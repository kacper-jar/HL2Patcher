import subprocess
import sys

class CommandRunnerService:
    """
    A class used to execute shell commands.
    """
    def __init__(self):
        pass

    def run_command(self, command):
        """
        Executes a shell command and raises an error if it fails.

        Args:
            command: Shell command to execute.
        """
        print(f"Executing: {command}")
        try:
            result = subprocess.run(command, shell=True, cwd=None, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {command}")
            print(e.stderr)
            raise SystemExit(e.stderr)