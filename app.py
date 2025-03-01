import logging

import flet as ft

from pages.before_patch_page import BeforePatchPage
from pages.patch_config_page import PatchConfigPage
from pages.start_page import StartPage
from services.page_navigation_service import PageNavigationService


class App:
    def __init__(self, page: ft.Page):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Initializing app...')

        self.__version__ = "1.0"
        page.title = "HL2Patcher"

        self.page = page
        self.nav_service = PageNavigationService(self)

        self.pages = {
            "start": StartPage(self),
            "before_patch": BeforePatchPage(self),
            "patch_config": PatchConfigPage(self),
        }
        self.current_page = "start"
        self.logger.info(f'App initialized. ({self.__version__})')

        self.build()

    def build(self):
        self.logger.info(f'Building page \'{self.current_page}\'...')
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
        self.logger.info(f'Page \'{self.current_page}\' built.')

    def navigate(self, page_name: str):
        self.current_page = page_name
        self.build()