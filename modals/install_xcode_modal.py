import flet as ft


class InstallXcodeModal(ft.AlertDialog):
    """
    Class representing modal that tells user how to install Xcode.
    """
    def __init__(self, on_close):
        """
        Args:
            on_close: function for closing the modal.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Installing Xcode")
        self.content = ft.Text("Open the App Store, search for Xcode, and click Get to start the download. Once the installation is complete, open Xcode to finish the initial setup.")
        self.actions = [
            ft.TextButton(
                "Close",
                on_click=on_close
            ),
        ]
