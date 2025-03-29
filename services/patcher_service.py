import logging
import os
import shutil

from modals.patch_in_progress_modal import PatchInProgressModal


class PatcherService:
    """
    A class used to patch the game.
    """
    def __init__(self, command_runner_service):
        self.command_runner_service = command_runner_service
        self.logger = logging.getLogger(__name__)

        self.repo_url = "https://github.com/nillerusr/source-engine.git"

    def apply_patch(self, working_dir: str, game_dir: str, modal: PatchInProgressModal):
        """
        Applies patch to the game.

        Args:
            working_dir: directory to keep temporary files in.
            game_dir: directory to copy patched fies to.
            modal: modal displaying patch progress.

        Returns:
            int: returns 0 if patch was applied successfully, 1 otherwise.
        """
        self.logger.info("Applying patch...")
        modal.set_total_tasks(5)
        try:
            modal.next_task("Preparing working directory...")
            if not os.path.exists(working_dir):
                os.makedirs(working_dir)

            modal.next_task("Cloning repository...")
            self.command_runner_service.run_command(f"git clone --recursive {self.repo_url} {working_dir}")

            modal.next_task("Building project...")
            os.chdir(working_dir)
            self.command_runner_service.run_command("python3 ./waf configure -T release --prefix='' --build-games=hl2")
            self.command_runner_service.run_command("python3 ./waf build")
            self.command_runner_service.run_command("python3 ./waf install --destdir='output'")

            modal.next_task("Replacing game files...")
            output_dir = os.path.join(working_dir, "output")
            if not os.path.exists(output_dir):
                self.logger.error("'output' directory was not created.")
                return 1

            hl2_osx_path = os.path.join(game_dir, "hl2_osx")
            if os.path.exists(hl2_osx_path):
                os.remove(hl2_osx_path)

            bin_paths = [os.path.join(game_dir, "bin"), os.path.join(game_dir, "hl2", "bin")]
            for path in bin_paths:
                if os.path.exists(path):
                    shutil.rmtree(path)

            shutil.copytree(os.path.join(output_dir, "bin"), os.path.join(game_dir, "bin"), dirs_exist_ok=True)
            shutil.copytree(os.path.join(output_dir, "hl2", "bin"), os.path.join(game_dir, "hl2", "bin"),
                            dirs_exist_ok=True)

            hl2_launcher_src = os.path.join(output_dir, "hl2_launcher")
            hl2_launcher_dest = os.path.join(game_dir, "hl2_launcher")
            shutil.copy2(hl2_launcher_src, hl2_launcher_dest)
            os.rename(hl2_launcher_dest, hl2_osx_path)

            return 0
        except Exception as e:
            self.logger.error(f"Error during applying patch: {e}")
            return 1
        finally:
            modal.set_task(5, "Cleaning up...")
            if os.path.exists(working_dir):
                shutil.rmtree(working_dir)
