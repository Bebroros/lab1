from pathlib import Path
import zipfile


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


def user_action():
    while True:
        action = input("Operation [d]ecompress or (q)uit: ")
        if action == "q":
            input("Press enter to quit")
            return quit()
        elif action == "d":
            kind_of_dec = input("Choose type of archive to decompress (zip/bzip2): ")
            if kind_of_dec == "bzip2":
                return "bzip2"
            if kind_of_dec == "zip":
                return "zip"
        print("Invalid input. Please try again.")


def decompress_zip(source_file: Path, output_dir: Path):
    with zipfile.ZipFile(source_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)


def decompress_bzip2():
    print("decompress_bzip2()")


def main():
    action = user_action()
    source_file, output_dir = path_directory()
    if action == "zip":
        decompress_zip(source_file, output_dir)
    if action == "bzip2":
        decompress_bzip2()


if __name__ == '__main__':
    main()
