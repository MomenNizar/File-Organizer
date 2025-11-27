# File Organizer

Keeping folders tidy can be a headache, especially when downloads, documents, and images pile up. Finding files becomes slow and frustrating.  

This Python script **automatically organizes files** in a folder by **file type (extension)** or **last modified date**, making it easy to:  

- Separate documents, images, videos, and other files  
- Quickly find files by type or date  
- Reduce clutter and keep your directories clean  
- Save time on manual sorting  

---

## Usage

```bash
python file_organizer.py --source /path/to/folder

Options

--dry-run – Show what would happen without moving files

--extensions – Only organize specific file types (e.g., .jpg .txt)

--method – Choose extension (default) or date

Examples

-Organize all files by extension:
    python file_organizer.py --source ~/Downloads
-Dry run (check what would happen without moving files):
    python file_organizer.py --source ~/Downloads --dry-run
-Organize only .jpg and .png files by date:
    python file_organizer.py --source ~/Pictures --method date --extensions .jpg .png

This tool is lightweight, requires no extra libraries, and is perfect for anyone who wants to automate file organization quickly and efficiently.