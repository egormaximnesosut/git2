#!/usr/bin/env python3
# file_counter.pyimport os
import argparse

def count_items(path):
    files = 0
    dirs = 0
    for root, dirnames, filenames in os.walk(path):
        # считаем все вложенные папки и файлы
        dirs += len(dirnames)
        files += len(filenames)
    return files, dirs

def main():
    parser = argparse.ArgumentParser(description="Count files and directories in a path")
    parser.add_argument('path', nargs='?', default='.', help='Path to count (default: current directory)')
    args = parser.parse_args()
    files, dirs = count_items(args.path)
    print(f"Path: {os.path.abspath(args.path)}")
    print(f"Files: {files}")
    print(f"Directories: {dirs}")

if name == "__main__":
    main()
