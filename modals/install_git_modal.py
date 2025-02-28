import flet as ft


class InstallGitModal(ft.AlertDialog):
    """
    Class representing modal that tells user how to install Git.
    """
    def __init__(self, on_close):
        """
        Args:
            on_close: function for closing the modal.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Installing Git")
        self.content = ft.Text("Git is included with the Xcode Command Line Tools. If it’s not installed, try reinstalling Xcode Command Line Tools.")
        self.actions = [
            ft.TextButton(
                "Close",
                on_click=on_close
            ),
        ]
