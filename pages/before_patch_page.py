import flet as ft


class BeforePatchPage:
    """
    Class representing 'Before Patch' page.
    """
    def __init__(self, app):
        self.app = app
        self.nav_service = app.nav_service

    def build(self):
        return ft.Column([
            ft.Row([
                ft.Text(
                    "Before You Start",
                    size=24,
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.DOWNLOAD),
                            title=ft.Text("Downgrade the Game"),
                            subtitle=ft.Text(
                                "To ensure everything works correctly, please make sure your game is on the pre-20th anniversary version, also known as the steam_legacy branch. This version of Half-Life 2 is required for HL2Patcher to function properly.\n\nYou can switch to the steam_legacy branch through the Steam client by right-clicking on the game, selecting “Properties”, and then choosing the appropriate branch under the “Betas” tab.\n\nOnce you’re all set, you can proceed with patching!")
                        )
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.WARNING),
                            title=ft.Text("Liability Disclaimer"),
                            subtitle=ft.Text(
                                "By using HL2Patcher, you acknowledge that you do so at your own risk. While the app is designed to help, the developer cannot be held responsible for any issues, including data loss, system instability, or other unintended consequences."),
                        )
                    ])
                )
            ),
            ft.Row([
                ft.TextButton(
                    "Back",
                    icon=ft.icons.ARROW_LEFT,
                    on_click=lambda e: self.nav_service.navigate_by_name("start")
                ),
                ft.TextButton(
                    "Next",
                    icon=ft.icons.ARROW_RIGHT,
                    on_click=lambda e: self.nav_service.navigate_by_name("patch_config")
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ])
