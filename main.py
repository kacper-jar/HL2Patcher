import flet as ft
import app as hlpatcher_app


def main(page: ft.Page):
    app = hlpatcher_app.App(page)
    page.on_route_change = app.navigate
    page.go("/")


ft.app(main)
