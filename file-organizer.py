#!/usr/bin/env python3
"""
Simple File Organizer
Moves files into folders by extension or date.
"""

import argparse
import logging
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def organize_file(file_path, method="extension", dry_run=False):
    """Move a single file into a folder based on the method"""
    try:
        # Decide folder name
        if method == "extension":
            folder_name = file_path.suffix[1:] or "no_extension"
        elif method == "date":
            date = datetime.fromtimestamp(file_path.stat().st_mtime).date()
            folder_name = str(date)
        else:
            folder_name = "other"

        target_folder = file_path.parent / folder_name

        # Make folder if it doesn't exist
        try:
            target_folder.mkdir(exist_ok=True)
        except Exception as e:
            logging.error(f"Couldn't create folder {target_folder}: {e}")
            return

        new_path = target_folder / file_path.name

        if dry_run:
            logging.info(f"[DRY-RUN] Would move: {file_path} -> {new_path}")
        else:
            try:
                file_path.rename(new_path)
                logging.info(f"Moved: {file_path} -> {new_path}")
            except Exception as e:
                logging.error(f"Failed to move {file_path}: {e}")

    except Exception as e:
        logging.error(f"Error handling file {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder")
    parser.add_argument("--source", required=True, help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually move files")
    parser.add_argument("--extensions", nargs="*", help="Only organize these file types")
    parser.add_argument("--method", choices=["extension", "date"], default="extension",
                        help="How to organize files")

    args = parser.parse_args()
    folder = Path(args.source)

    if not folder.exists() or not folder.is_dir():
        logging.error("Folder does not exist or is not a folder")
        return

    # Normalize extensions for comparison
    extensions = [ext.lower() for ext in args.extensions] if args.extensions else None

    for item in folder.iterdir():
        if item.is_file():
            if extensions and item.suffix.lower() not in extensions:
                continue
            organize_file(item, method=args.method, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
