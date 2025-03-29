import logging
import os


class ToolsCheckerService:
    """
    A class used to check if required tools and dependencies are installed.
    """
    def __init__(self, command_runner_service):
        self.command_runner_service = command_runner_service
        self.logger = logging.getLogger(__name__)

    def check_tools(self):
        """
        Checks if Python, Xcode, Xcode CLI tools, Homebrew and Homebrew packages (dependencies) are installed.

        Returns: dict: returns dictionary with tool names as keys and their install status as values. The value is
        True if installed or False if it's not installed.
        """
        status = {
            "python3": self.check_python(),
            "xcode": self.check_xcode(),
            "xcode-cli": self.check_xcode_cli(),
            "git": self.check_git(),
            "homebrew": self.check_homebrew(),
            "homebrew-packages": self.check_homebrew_packages()
        }
        self.logger.info(f"Tools installed: {status}")
        return status

    def check_python(self) -> bool:
        try:
            self.command_runner_service.run_command("python3 --version")
            return True
        except SystemExit:
            return False

    def check_xcode(self) -> bool:
        xcode_installed = os.path.exists("/Applications/Xcode.app")
        return xcode_installed

    def check_xcode_cli(self) -> bool:
        try:
            self.command_runner_service.run_command("xcode-select --version")
            return True
        except SystemExit:
            return False

    def check_git(self) -> bool:
        try:
            self.command_runner_service.run_command("git --version")
            return True
        except SystemExit:
            return False

    def check_homebrew(self) -> bool:
        try:
            self.command_runner_service.run_command("brew --version")
            return True
        except SystemExit:
            return False

    def check_homebrew_packages(self) -> bool:
        packages = ["sdl2", "freetype2", "fontconfig", "pkg-config", "opus", "libpng", "libedit"]
        all_packages_installed = True
        for package in packages:
            try:
                self.command_runner_service.run_command(f"brew list --versions {package}")
            except SystemExit:
                all_packages_installed = False
                break
        return all_packages_installed
