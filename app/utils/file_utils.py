import os

def cleanup_temp_files(paths: list[str]):
    """Placeholder utility for removing temporary files."""
    for path in paths:
        try:
            os.remove(path)
        except FileNotFoundError:
            continue
