import flet as ft

class StartPage:
    def __init__(self, app):
        self.app = app
        self.nav_service = app.nav_service

    def build(self):
        return ft.Column([
            ft.Text('StartPage'),
        ])