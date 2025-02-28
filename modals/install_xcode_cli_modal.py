import flet as ft
import pyperclip


class InstallXcodeCliModal(ft.AlertDialog):
    """
    Class representing modal that tells user how to install Xcode Command Line Tools.
    """
    def __init__(self, on_close):
        """
        Args:
            on_close: function for closing the modal.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Installing Xcode Command Line Tools")
        self.content = ft.Text("Click the “Copy command” button below, paste the command into Terminal, and press Enter. A prompt will appear — follow the on-screen instructions to complete the installation.")
        self.actions = [
            ft.TextButton(
                "Copy Command",
                on_click=lambda e: pyperclip.copy(
                    "xcode-select --install"
                )
            ),
            ft.TextButton(
                "Close",
                on_click=on_close
            ),
        ]
