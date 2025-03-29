import logging
import subprocess


class CommandRunnerService:
    """
    A class used to execute shell commands.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run_command(self, command):
        """
        Executes a shell command and raises an error if it fails.

        Args:
            command: Shell command to execute.
        """
        self.logger.info(f"Executing: {command}")
        try:
            result = subprocess.run(command, shell=True, cwd=None, check=True, text=True, capture_output=True)
            self.logger.info(f"Output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error executing command: {command}")
            self.logger.error(e.stderr)
            raise SystemExit(e.stderr)
