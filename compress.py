import datetime
from pathlib import Path
import zipfile
import gzip


def generate_archive_name(filename, outdir) -> str:
    counter = 1
    while True:
        name = f"{filename}_{datetime.date.today().strftime('%Y%m%d')}_{counter}"
        if Path(f"{outdir}/{name}.zip").exists() or Path(f"{outdir}/{name}.gz").exists():
            counter += 1
        else:
            print(outdir / name)
            return name


def compress_to_zip(indir, outdir, filename, extension='*') -> None:
    with zipfile.ZipFile(outdir / f'{filename}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        if indir.is_dir():
            list_of_files = [file for file in indir.rglob(f'{extension}') if file.is_file()
                             and file != outdir / f'{filename}.zip']
            for file in list_of_files:
                zip_file.write(file, file.relative_to(indir))
        else:
            zip_file.write(indir, indir.name)
    print("Zip file created!")


def compress_to_gzip(indir, outdir, filename) -> None:
    with open(indir, 'rb') as file:
        data = file.read()
        with gzip.open(outdir / f'{filename}.gz', 'wb') as gzip_file:
            gzip_file.write(data)
    print("Gzip file created!")


def ask_users_directory():
    while True:
        indir = Path(input("Enter path to your file: "))
        if indir.exists():
            break
        print("Directory does not exist. Please try again.")
    while True:
        outdir = Path(input("Enter path to output directory: "))
        if outdir.exists():
            break
        print("Directory does not exist. Please try again.")
    return indir, outdir


def user_action():
    while True:
        action = input("What do you want to do? (C)ompress, (Q)uit:")
        if action.lower() == "q":
            print("Thank you!")
            input("Press enter to quit")
            return quit()
        elif action.lower() == "c":
            type_of_archive = input("What type of archive do you want to compress(zip, gzip)?")
            if type_of_archive.lower() == "zip":
                return 'zip'
            elif type_of_archive.lower() == "gzip":
                return 'gzip'
            else:
                print("Invalid input. Please try again.")
                pass
        else:
            print("Invalid input. Please try again.")
            pass


def main():
    while True:
        action = user_action()
        #indir, outdir = ask_users_directory()
        indir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2\bebra')
        outdir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2\bebra')
        filename = input("Enter name of archive: ")
        if action == 'zip':
            compress_to_zip(indir, outdir, generate_archive_name(filename, outdir))
        elif action == 'gzip':
            compress_to_gzip(indir, outdir, generate_archive_name(filename, outdir))


if __name__ == '__main__':
    main()
