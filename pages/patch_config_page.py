import flet as ft
import sys

from modals.patch_failed_modal import PatchFailedModal
from modals.patch_in_progress_modal import PatchInProgressModal
from modals.patch_successful_modal import PatchSuccessfulModal
from services.command_runner_service import CommandRunnerService
from services.patcher_service import PatcherService


class PatchConfigPage:
    def __init__(self, app):
        self.app = app
        self.nav_service = app.nav_service

        self.working_dir = "/tmp/HL2Patcher/working"
        self.game_dir = None

        self.working_dir_picker = ft.FilePicker(
            on_result=lambda e: self.update_working_dir_path(e.path)
        )
        self.game_dir_picker = ft.FilePicker(
            on_result=lambda e: self.update_game_dir_path(e.path)
        )
        app.page.overlay.extend([self.working_dir_picker, self.game_dir_picker])

        self.patch_in_progress_modal = PatchInProgressModal()
        self.patch_successful_modal = PatchSuccessfulModal(
            exit=self.handle_exit
        )
        self.patch_failed_modal = PatchFailedModal(
            exit=self.handle_exit
        )

        self.command_runner_service = CommandRunnerService()
        self.patcher_service = PatcherService(
            command_runner_service=self.command_runner_service
        )

    def build(self):
        return ft.Column([
            ft.Row([
                ft.Text(
                    "Configure Patch",
                    size=24,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.FOLDER),
                            title=ft.Text("Working directory"),
                            subtitle=ft.Text("Choose a folder where HL2Patcher will store temporary files during the patching process. Make sure there’s enough free space.")
                        ),
                        ft.Row(
                            controls=[
                                ft.TextField(
                                    expand=True,
                                    read_only=True,
                                    value=self.working_dir
                                ),
                                ft.IconButton(
                                    icon=ft.icons.FOLDER,
                                    on_click=lambda e: self.working_dir_picker.get_directory_path()
                                )
                            ]
                        )
                    ]),
                    padding=10
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.FOLDER),
                            title=ft.Text("Game install directory"),
                            subtitle=ft.Text("Enter the path to your Half-Life 2 install directory. You can find it by right-clicking the game in Steam, selecting “Properties”, then “Local Files”, and clicking “Browse”.")
                        ),
                        ft.Row(
                            controls=[
                                ft.TextField(
                                    expand=True,
                                    read_only=True,
                                    value=self.game_dir
                                ),
                                ft.IconButton(
                                    icon=ft.icons.FOLDER,
                                    on_click=lambda e: self.game_dir_picker.get_directory_path()
                                )
                            ]
                        )
                    ]),
                    padding=10
                )
            ),
            ft.Row([
                ft.TextButton(
                    "Back",
                    icon=ft.icons.ARROW_LEFT,
                    on_click=lambda e: self.nav_service.navigate_by_name("before_patch")
                ),
                ft.TextButton(
                    "Patch",
                    icon=ft.icons.INSTALL_DESKTOP,
                    on_click=lambda e: self.apply_patch(),
                    disabled=not self.is_patch_button_enabled()
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ])

    def update_working_dir_path(self, path):
        if path is not None:
            self.working_dir = path
            self.nav_service.reload([self.working_dir, self.game_dir])

    def update_game_dir_path(self, path):
        if path is not None:
            self.game_dir = path
            self.nav_service.reload([self.working_dir, self.game_dir])

    def is_patch_button_enabled(self):
        if self.working_dir is not None and self.game_dir is not None:
            return True
        return False

    def apply_patch(self):
        self.app.page.open(self.patch_in_progress_modal)
        if self.patcher_service.apply_patch(self.working_dir, self.game_dir, self.patch_in_progress_modal) == 0:
            self.app.page.close(self.patch_in_progress_modal)
            self.app.page.open(self.patch_successful_modal)
        else:
            self.app.page.close(self.patch_in_progress_modal)
            self.app.page.open(self.patch_failed_modal)

    def handle_exit(self):
        self.app.page.window.close()