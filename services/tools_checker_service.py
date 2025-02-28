import os

class ToolsCheckerService:
    """
    A class used to check if required tools and dependencies are installed.
    """
    def __init__(self, command_runner_service):
        self.command_runner_service = command_runner_service

    def check_tools(self):
        """
        Checks if Python, Xcode, Xcode CLI tools, Homebrew and Homebrew packages (dependencies) are installed.
        """
        status = {}

        try:
            self.command_runner_service.run_command("python3 --version")
            status["python3"] = True
        except SystemExit:
            status["python3"] = False

        xcode_installed = os.path.exists("/Applications/Xcode.app")
        status["xcode"] = xcode_installed

        try:
            self.command_runner_service.run_command("xcode-select --version")
            status["xcode-cli"] = True
        except SystemExit:
            status["xcode-cli"] = False

        try:
            self.command_runner_service.run_command("git --version")
            status["git"] = True
        except SystemExit:
            status["git"] = False

        try:
            self.command_runner_service.run_command("brew --version")
            status["homebrew"] = True
        except SystemExit:
            status["homebrew"] = False

        packages = ["sdl2", "freetype2", "fontconfig", "pkg-config", "opus", "libpng", "libedit"]
        all_packages_installed = True
        for package in packages:
            try:
                self.command_runner_service.run_command(f"brew list --versions {package}")
            except SystemExit:
                all_packages_installed = False
                break

        status["homebrew-packages"] = all_packages_installed

        return status