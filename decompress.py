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


def user_action():
    while True:
        action = input("Operation [d]ecompress or (q)uit: ")
        if action == "q":
            input("Press enter to quit")
            return quit()
        elif action == "d":
            kind_of_dec = input("Choose type of archive to decompress (bzip2/xz): ")
            if kind_of_dec == "bzip2":
                return "bzip2"
            if kind_of_dec == "xz":
                return "xz"
        pass
        print("Invalid input. Please try again.")


def main():
    user_action()


if __name__ == '__main__':
    main()
