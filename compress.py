import datetime
from pathlib import Path
import zipfile
import gzip


def generate_archive_name(filename, outdir) -> str:
    counter = 1
    while True:
        name = f"{filename}_{datetime.date.today().strftime('%Y%m%d')}_{counter}"
        if not Path(f"{outdir}/{name}.zip").exists() or Path(f"{outdir}/{name}.gzip").exists():
            print(outdir/name)
            return name
        counter += 1


def compress_to_zip(indir, outdir, filename) -> None:
    with zipfile.ZipFile(outdir/f'{filename}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        if indir.is_dir():
            list_of_files = [file for file in indir.rglob('*') if file.is_file() and file != outdir/f'{filename}.zip']
            for file in list_of_files:
                zip_file.write(file, file.name)
        else:
            zip_file.write(indir, indir.name)
    print("Zip file created!")


def compress_to_gzip(indir, outdir, filename) -> None:
    print(filename)
    with gzip.open(outdir/f'{filename}.gzip', 'wt') as gzip_file:
        gzip_file.write(str(indir))
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


def main():
    #indir, outdir = ask_users_directory()
    indir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2\bebra\birthday.txt')
    outdir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2\bebra')
    filename = input("Enter name of archive: ")
    compress_to_zip(indir, outdir, generate_archive_name(filename, outdir))
    compress_to_gzip(indir, outdir, generate_archive_name(filename, outdir))


if __name__ == '__main__':
    main()
