import flet as ft
import logging
import os
import app as hlpatcher_app


def main(page: ft.Page):
    log_path = "/tmp/HL2Patcher/"
    log_filename = "HL2Patcher.log"
    log_file = os.path.join(log_path, log_filename)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    logger.info("Logger initialized")

    # Ensure Homebrew is in PATH when running the app, it fixes issues with Homebrew
    homebrew_path = "/opt/homebrew/bin/brew"
    os.environ["PATH"] += f":{os.path.dirname(homebrew_path)}"

    app = hlpatcher_app.App(page)
    page.on_route_change = app.navigate


ft.app(main)
