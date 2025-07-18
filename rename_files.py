import os

def rename_files_and_folders(base_path, replacements):
    """Recursively rename files and folders based on replacements."""
    for dirpath, dirnames, filenames in os.walk(base_path, topdown=False):
        # Rename files
        for filename in filenames:
            new_filename = filename
            for old, new in replacements.items():
                new_filename = new_filename.replace(old, new)
            if new_filename != filename:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)

        # Rename directories
        for dirname in dirnames:
            new_dirname = dirname
            for old, new in replacements.items():
                new_dirname = new_dirname.replace(old, new)
            if new_dirname != dirname:
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, new_dirname)
                os.rename(old_path, new_path)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    base_folder = input(f"Enter datapack root folder path (or leave empty to use this script's folder: {script_dir}): ").strip()
    if not base_folder:
        base_folder = script_dir

    namespace = input("Enter your namespace (to replace 'template'): ").strip()
    aspect_name = input("Enter your aspect name (to replace 'example'): ").strip()

    replacements = {
        'template': namespace,
        'example': aspect_name
    }

    rename_files_and_folders(base_folder, replacements)

    print(f"\n✔️ Folder and file names updated successfully in: {base_folder}")
    input("\nPress Enter to exit...")
