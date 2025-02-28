import flet as ft


class InstallPythonModal(ft.AlertDialog):
    """
    Class representing modal that tells user how to install python.
    """
    def __init__(self, on_close):
        """
        Args:
            on_close: function for closing the modal.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Installing Python 3")
        self.content = ft.Text("To install Python 3, go to python.org/downloads and download the latest macOS 64-bit installer. Open the downloaded .pkg file and follow the on-screen instructions to complete the installation. Once installed, Python 3 will be ready to use.")
        self.actions = [
            ft.TextButton(
                "Close",
                on_click=on_close
            ),
        ]
