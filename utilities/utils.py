"""
Module of all utilities for the project.
"""
import os


def get_root_path() -> str:
    """
    Get the root path of the project directory.

    Returns:
        str: The root path of the current project directory.
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(dir_path)

    return root_path
