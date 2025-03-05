import logging
import platform

class SystemCheckerService:
    """
    A class used to check if system is supported.
    """
    def __init__(self, app):
        self.app = app
        self.nav_service = app.nav_service

        self.logger = logging.getLogger(__name__)

    def check_system(self):
        """
        Checks if the system is running macOS 11 Big Sur or newer.

        Returns:
            bool: True if the system is macOS 11 or newer, False otherwise.
        """
        if platform.system() != "Darwin":
            logging.critical(f"Not supported operating systems. {platform.system()}")
            return False

        mac_version = platform.mac_ver()[0]
        if not mac_version:
            logging.critical(f"Not supported macOS version. Trying to run on MacOS {platform.mac_ver()[0]}")
            return False
        major_version = int(mac_version.split(".")[0])
        return major_version >= 11