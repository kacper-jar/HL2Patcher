import flet as ft

class NotSupportedPage:
    def __init__(self, app):
        self.app = app

    def build(self):
        return ft.Column([
            ft.Text("NotSupportedPage")
        ])