import flet as ft

class PatchConfigPage:
    def __init__(self, app):
        self.app = app

    def build(self):
        return ft.Column([
            ft.Row([
                ft.Text(
                    "Configure Patch",
                    size=24,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.WARNING),
                            title=ft.Text("Before You Start"),
                            subtitle=ft.Text("To ensure everything works correctly, please make sure your game is on the pre-20th anniversary version, also known as the steam_legacy branch. This version of Half-Life 2 is required for HL2Patcher to function properly.\n\nYou can switch to the steam_legacy branch through the Steam client by right-clicking on the game, selecting “Properties”, and then choosing the appropriate branch under the “Betas” tab.\n\nOnce you’re all set, you can proceed with patching!")
                        )
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.FOLDER),
                            title=ft.Text("Game install directory"),
                            subtitle=ft.Text("Enter the path to your Half-Life 2 install directory. You can find it by right-clicking the game in Steam, selecting “Properties”, then “Local Files”, and clicking “Browse”.")
                        ),
                        ft.Row(
                            controls=[
                                ft.TextField(
                                    expand=True,
                                    read_only=True
                                ),
                                ft.IconButton(
                                    icon=ft.icons.FOLDER,
                                )
                            ]
                        )
                    ]),
                    padding=10
                )
            ),
            ft.Row([
                ft.TextButton(
                    "Patch",
                    icon=ft.icons.INSTALL_DESKTOP,
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ])