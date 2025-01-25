import flet as ft

class PatchConfigPage:
    def __init__(self, app):
        self.app = app

    def build(self):
        return ft.Column([
            ft.Text("PatchConfigPage")
        ])