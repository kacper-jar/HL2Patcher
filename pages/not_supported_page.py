import flet as ft


class NotSupportedPage:
    def __init__(self, app):
        self.app = app

    def build(self):
        return ft.Column([
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.WARNING),
                            title=ft.Text("Unsupported OS"),
                            subtitle=ft.Text("HL2Patcher is only compatible with macOS 11 or newer. Running it on an unsupported system will prevent it from working properly. Please update your macOS or use a supported device."),
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton(
                                    icon=ft.icons.EXIT_TO_APP,
                                    text="Exit",
                                    on_click=lambda e: self.handle_exit()
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ]),
                    padding=10
                ),
                expand=True
            )
        ])

    def handle_exit(self):
        self.app.page.window.close()
