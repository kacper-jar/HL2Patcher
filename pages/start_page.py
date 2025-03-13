import flet as ft
import webbrowser

from modals.install_git_modal import InstallGitModal
from modals.install_homebrew_modal import InstallHomebrewModal
from modals.install_homebrew_packages_modal import InstallHomebrewPackagesModal
from modals.install_python_modal import InstallPythonModal
from modals.install_xcode_cli_modal import InstallXcodeCliModal
from modals.install_xcode_modal import InstallXcodeModal
from services.command_runner_service import CommandRunnerService
from services.tools_checker_service import ToolsCheckerService


class StartPage:
    """
    Class representing 'Start' page.
    """
    def __init__(self, app):
        self.app = app
        self.nav_service = app.nav_service

        self.command_runner_service = CommandRunnerService()
        self.tools_checker_service = ToolsCheckerService(self.command_runner_service)

        self.python_modal = InstallPythonModal(
            on_close=lambda e: self.close_python_modal()
        )
        self.xcode_modal = InstallXcodeModal(
            on_close=lambda e: self.close_xcode_modal()
        )
        self.xcode_cli_modal = InstallXcodeCliModal(
            on_close=lambda e: self.close_xcode_cli_modal()
        )
        self.git_modal = InstallGitModal(
            on_close=lambda e: self.close_git_modal()
        )
        self.homebrew_modal = InstallHomebrewModal(
            on_close=lambda e: self.close_homebrew_modal()
        )
        self.dependencies_modal = InstallHomebrewPackagesModal(
            on_close=lambda e: self.close_dependencies_modal(),
        )

    def build(self):
        check_result = self.tools_checker_service.check_tools()

        return ft.Column([
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Image(
                                src=f"../assets/icon.png",
                                fit=ft.ImageFit.CONTAIN
                            ),
                            title=ft.Text(f'Welcome to HL2Patcher ({self.app.__version__})'),
                            subtitle=ft.Text('HL2Patcher makes Half-Life 2 playable on modern ARM Macs that only support 64-bit apps. Its goal is to simplify the process into an easy-to-use app, so anyone can enjoy the game again without hassle.'),
                            trailing=ft.IconButton(
                                ft.icons.BUG_REPORT,
                                tooltip="Bug Report",
                                on_click=lambda e: webbrowser.open("https://github.com/kacper-jar/HL2Patcher/issues/new?template=bug_report.md")
                            )
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
                            subtitle=ft.Text("To use HL2Patcher, you’ll need a few essential tools to ensure everything runs smoothly. These tools are required to properly patch the game.\n\nMake sure to check that you have all the necessary components before continuing. If you need help to install any of these tools click question mark."),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(self.get_icon(check_result, "python3")),
                            title=ft.Text("Python 3"),
                            subtitle=ft.Text("Required for compiling project via WAF build system."),
                            trailing=ft.IconButton(
                                ft.icons.HELP_ROUNDED,
                                on_click=lambda e: self.open_python_modal()
                            )
                        ),
                        ft.ListTile(
                            leading=ft.Icon(self.get_icon(check_result, "xcode")),
                            title=ft.Text("Xcode"),
                            subtitle=ft.Text("Required for compiling files and ensuring the app works correctly."),
                            trailing=ft.IconButton(
                                ft.icons.HELP_ROUNDED,
                                on_click=lambda e: self.open_xcode_modal()
                            )
                        ),
                        ft.ListTile(
                            leading=ft.Icon(self.get_icon(check_result, "xcode-cli")),
                            title=ft.Text("Xcode Command Line Tools"),
                            subtitle=ft.Text("Needed for various build tasks."),
                            trailing=ft.IconButton(
                                ft.icons.HELP_ROUNDED,
                                on_click=lambda e: self.open_xcode_cli_modal()
                            )
                        ),
                        ft.ListTile(
                            leading=ft.Icon(self.get_icon(check_result, "git")),
                            title=ft.Text("Git"),
                            subtitle=ft.Text("A version control tool required for downloading necessary files during the patching process."),
                            trailing=ft.IconButton(
                                ft.icons.HELP_ROUNDED,
                                on_click=lambda e: self.open_git_modal()
                            )
                        ),
                        ft.ListTile(
                            leading=ft.Icon(self.get_icon(check_result, "homebrew")),
                            title=ft.Text("Homebrew"),
                            subtitle=ft.Text("A package manager used to install necessary dependencies."),
                            trailing=ft.IconButton(
                                ft.icons.HELP_ROUNDED,
                                on_click=lambda e: self.open_homebrew_modal()
                            )
                        ),
                        ft.ListTile(
                            leading=ft.Icon(self.get_icon(check_result, "homebrew-packages")),
                            title=ft.Text("Build Dependencies"),
                            subtitle=ft.Text("Additional tools required by HL2Patcher, installed through Homebrew."),
                            trailing=ft.IconButton(
                                ft.icons.HELP_ROUNDED,
                                on_click=lambda e: self.open_dependencies_modal()
                            )
                        )
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            title=ft.Text("Re-verify tool installation"),
                            trailing=ft.TextButton(
                                text="Refresh",
                                icon=ft.icons.REFRESH,
                                on_click=lambda e: self.refresh()
                            )
                        )
                    ])
                )
            ),
            ft.Row([
                ft.TextButton(
                    "Next",
                    icon=ft.icons.ARROW_RIGHT,
                    on_click=lambda e: self.nav_service.navigate_by_name("before_patch"),
                    disabled=not self.is_next_button_enabled(check_result),
                    tooltip="" if self.is_next_button_enabled(check_result) else "Check the list above, install missing tools and restart the app."
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ])

    def get_icon(self, status, tool_id):
        if status[tool_id]:
            return ft.icons.CHECK_CIRCLE
        else:
            return ft.icons.REMOVE_CIRCLE

    def is_next_button_enabled(self, check_result):
        all_installed = all(check_result.values())
        return all_installed

    def open_python_modal(self):
        self.app.page.open(self.python_modal)

    def close_python_modal(self):
        self.app.page.close(self.python_modal)

    def open_xcode_modal(self):
        self.app.page.open(self.xcode_modal)

    def close_xcode_modal(self):
        self.app.page.close(self.xcode_modal)

    def open_xcode_cli_modal(self):
        self.app.page.open(self.xcode_cli_modal)

    def close_xcode_cli_modal(self):
        self.app.page.close(self.xcode_cli_modal)

    def open_git_modal(self):
        self.app.page.open(self.git_modal)

    def close_git_modal(self):
        self.app.page.close(self.git_modal)

    def open_homebrew_modal(self):
        self.app.page.open(self.homebrew_modal)

    def close_homebrew_modal(self):
        self.app.page.close(self.homebrew_modal)

    def open_dependencies_modal(self):
        self.app.page.open(self.dependencies_modal)

    def close_dependencies_modal(self):
        self.app.page.close(self.dependencies_modal)

    def refresh(self):
        self.nav_service.reload()