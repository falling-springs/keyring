"""
Hook used by pyinstaller to expose hidden imports.
"""

from keyring.py312compat import metadata

hiddenimports = [ep.value for ep in metadata.entry_points(group='keyring.backends')]
