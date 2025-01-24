import flet as ft

from src.pages.patch_config_page import PatchConfigPage
from src.pages.start_page import StartPage
from src.services.page_navigation_service import PageNavigationService


class App:
    def __init__(self, page: ft.Page):
        page.title = "HL2Patcher"
        self.page = page
        self.nav_service = PageNavigationService(self)

        self.pages = {
            "start": StartPage(self),
            "patch_config": PatchConfigPage(self),
        }
        self.current_page = "start"

        self.build()

    def build(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                controls=[
                    ft.Row([
                        ft.Column([
                            self.pages[self.current_page].build()
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        expand=True
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    expand=True
                    )
                ]
            )
        )
        self.page.update()

    def navigate(self, page_name: str):
        self.current_page = page_name
        self.build()