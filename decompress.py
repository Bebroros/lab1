from pathlib import Path


def path_directory():
    while True:
        source_file = Path(input("Enter path to your file: "))
        if source_file.exists():
            break
        print("Directory does not exist. Please try again.")
    while True:
        output_dir = Path(input("Enter path to output directory: "))
        if output_dir.exists():
            break
        print("Directory does not exist. Please try again.")
    return source_file, output_dir


def main():
    path_directory()


if __name__ == '__main__':
    main()
