import datetime
from pathlib import Path


def generate_archive_name(filename, outdir) -> str:
    counter = 1
    today = datetime.date.today().strftime('%Y%m%d')
    while True:
        name = f"{filename}_{today}_{counter}"
        if not Path(outdir/name).exists():
            return name
        counter += 1


def compress_to_zip(indir, outdir, filename) -> None:
    print("helo")


def main():
    indir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2\bebra.txt')
    outdir = Path(r'C:\Users\retro\PycharmProjects\pythonProject2')
    filename = input("Enter name of archive: ")
    compress_to_zip(indir, outdir, generate_archive_name(filename, outdir))


if __name__ == '__main__':
    main()
