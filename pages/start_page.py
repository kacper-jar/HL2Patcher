import flet as ft

class StartPage:
    def __init__(self, app):
        self.app = app
        self.nav_service = app.nav_service

    def build(self):
        return ft.Column([
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Image(
                                src=f"../assets/icon.png",
                                fit=ft.ImageFit.CONTAIN
                            ),
                            title=ft.Text('Welcome to HL2Patcher'),
                            subtitle=ft.Text('HL2Patcher makes Half-Life 2 playable on modern ARM Macs that only support 64-bit apps. Its goal is to simplify the process into an easy-to-use app, so anyone can enjoy the game again without hassle.'),
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
                            subtitle=ft.Text("By using HL2Patcher, you acknowledge that you do so at your own risk. While the app is designed to help, the developer cannot be held responsible for any issues, including data loss, system instability, or other unintended consequences."),
                        )
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.BUILD),
                            title=ft.Text("Required Tools"),
                            subtitle=ft.Text("To use HL2Patcher, you’ll need a few essential tools to ensure everything runs smoothly. These tools are required to properly patch the game.\n\nMake sure to check that you have all the necessary components before continuing. If you need help to install any of theese tools click question mark."),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.CHECK_CIRCLE),
                            title=ft.Text("Xcode"),
                            subtitle=ft.Text("Required for compiling files and ensuring the app works correctly."),
                            trailing=ft.Icon(ft.icons.HELP_ROUNDED)
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.REMOVE_CIRCLE),
                            title=ft.Text("Xcode Command Line Tools"),
                            subtitle=ft.Text("Needed for various build tasks."),
                            trailing=ft.Icon(ft.icons.HELP_ROUNDED)
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.REMOVE_CIRCLE),
                            title=ft.Text("HomeBrew"),
                            subtitle=ft.Text("A package manager used to install necessary dependencies."),
                            trailing=ft.Icon(ft.icons.HELP_ROUNDED)
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.REMOVE_CIRCLE),
                            title=ft.Text("Dependencies"),
                            subtitle=ft.Text("Additional tools required by HL2Patcher, installed through Homebrew."),
                            trailing=ft.Icon(ft.icons.HELP_ROUNDED)
                        )
                    ])
                )
            ),
            ft.Row([
                ft.TextButton(
                    "Next",
                    icon=ft.icons.ARROW_RIGHT,
                    on_click=lambda e: self.nav_service.navigate_by_name("patch_config")
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ])
