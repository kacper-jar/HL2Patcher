import flet as ft


class PatchSuccessfulModal(ft.AlertDialog):
    """
    Class representing modal for successful patch.
    """
    def __init__(self, exit):
        """
        Args:
            exit: function closing the app.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Patch Complete!")
        self.content = ft.Text("HL2Patcher has successfully applied the patch. You can now launch Half-Life 2 and enjoy the game on your Mac.")
        self.actions = [
            ft.TextButton(
                "Exit",
                on_click=lambda e: exit()
            ),
        ]