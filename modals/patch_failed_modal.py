import flet as ft


class PatchFailedModal(ft.AlertDialog):
    """
    Class representing modal for successful patch.
    """
    def __init__(self, exit):
        """
        Args:
            exit: function closing the app
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Patch Failed")
        self.content = ft.Text("An error occurred during the patching process. Please check your internet connection and ensure all required tools are installed and up to date.\nIf the issue persists, try running the patch again or report an issue (the button is located at the top of the start page).")
        self.actions = [
            ft.TextButton(
                "Exit",
                on_click=lambda e: exit()
            ),
        ]