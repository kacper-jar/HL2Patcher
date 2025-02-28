import flet as ft
import pyperclip


class InstallHomebrewPackagesModal(ft.AlertDialog):
    """
    Class representing modal that tells user how to install HomeBrew packages (dependencies).
    """
    def __init__(self, on_close):
        """
        Args:
            on_close: function for closing the modal.
        """
        super().__init__()
        self.modal = True
        self.title = ft.Text("Installing dependencies (via HomeBrew)")
        self.content = ft.Text("Click the “Copy command” button below, paste the command into Terminal, and press Enter to install dependencies.")
        self.actions = [
            ft.TextButton(
                "Copy Command",
                on_click=lambda e: pyperclip.copy(
                    "brew install sdl2 freetype2 fontconfig pkg-config opus libpng libedit"
                )
            ),
            ft.TextButton(
                "Close",
                on_click=on_close
            )
        ]