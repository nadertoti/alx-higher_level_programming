#!/usr/bin/python3
"""Module for lookup method."""


class MyList(list):
    """Custom the list."""
    def print_sorted(self):
        """Approuch for print sorted list."""
        print(sorted(self))
