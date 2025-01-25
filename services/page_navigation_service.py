from typing import Optional, Any


class PageNavigationService:
    """
    A class used to navigate between pages with ability to pass arguments.
    """
    def __init__(self, app):
        self.app = app

    def navigate_by_name(self, page_name: str, args: Optional[dict[str, Any]] = None):
        """
        Changes the currently displayed page using name.

        Args:
            page_name: name of the page to navigate to.
            args: arguments to pass to the page.
        """
        self.app.page.session.set("nav_page", page_name)
        self.app.page.session.set("nav_args", args)
        self.app.navigate(page_name)

    def reload(self, args: Optional[dict[str, Any]] = None):
        """
        Forces the current page to reload.
        """
        self.navigate_by_name(self.get_page_name(), args)

    def get_page_name(self):
        """
        Retrieves the currently displayed page name.

        Returns:
            str: name of the currently displayed page.
        """
        return self.app.page.session.get("nav_page")

    def get_args(self):
        """
        Retrieves arguments passed to the current page.

        Returns:
            dict: returns dictionary of arguments passed to the current page.
        """
        return self.app.page.session.get("nav_args")
