import flet as ft


class InstallHomebrewModal(ft.AlertDialog):
    """
    Class representing modal that tells user how to install HomeBrew.
    """
    def __init__(self, on_close):
        """
        Args:
            on_close: function for closing the modal.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Installing HomeBrew")
        self.content = ft.Text("Go to brew.sh and copy the installation command from the website. Open Terminal, paste the command, and press Enter. Follow the on-screen instructions to complete the installation.")
        self.actions = [
            ft.TextButton(
                "Close",
                on_click=on_close
            ),
        ]
