import datetime
from pathlib import Path
import zipfile


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
        zip_file.write(indir, indir.name)
    print("Zip file created!")


def main():
    indir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2\birthday.txt')
    outdir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2')
    filename = input("Enter name of archive: ")
    compress_to_zip(indir, outdir, generate_archive_name(filename, outdir))


if __name__ == '__main__':
    main()
