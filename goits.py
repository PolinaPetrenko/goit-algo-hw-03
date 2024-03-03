import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            dest_subdir = os.path.join(dest_dir, extension)
            os.makedirs(dest_subdir, exist_ok=True)
            dest_file = os.path.join(dest_subdir, file)
            shutil.copy(source_file, dest_file)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py source_dir [destination_dir]")
        return

    source_dir = sys.argv[1]
    if not os.path.isdir(source_dir):
        print("Error: Source directory does not exist.")
        return

    dest_dir = "dist"
    if len(sys.argv) >= 3:
        dest_dir = sys.argv[2]

    copy_files(source_dir, dest_dir)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()

