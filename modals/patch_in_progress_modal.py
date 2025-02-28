import flet as ft


class PatchInProgressModal(ft.AlertDialog):
    """
    Class representing modal that tells user current step of patching progress.
    """
    def __init__(self):
        super().__init__()
        self.modal = True
        self.title = ft.Text("Patching...")
        self.content = None

        self.current_task = 0
        self.total_tasks = 1

    def set_total_tasks(self, total_tasks):
        """
        Sets total number of tasks.

        Args:
            total_tasks: The total number of tasks.
        """
        self.total_tasks = total_tasks

    def set_task(self, task_id, task_name):
        """
        Sets current task.

        Args:
            task_id: Current task number.
            task_name: Task name.
        """
        self.current_task = task_id
        self.content = ft.Text(f"The patching process is underway and may take a few minutes. Please ensure you have a stable internet connection to avoid any issues while downloading files from GitHub.\nCurrent task ({self.current_task}/{self.total_tasks}): {task_name}")
        self.update()

    def next_task(self, task_name):
        """
        Advances to next task.

        Args:
            task_name: Task name.
        """
        self.set_task(self.current_task + 1, task_name)