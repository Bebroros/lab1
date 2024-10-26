import argparse
import datetime
from pathlib import Path
import zipfile
import tarfile
import sys


def generate_archive_name(indir, outdir) -> str:
    if indir.is_file():
        filename = indir.parent.name
    else:
        filename = indir.name
    counter = 1
    while True:
        name = f"{filename}_{datetime.date.today().strftime('%Y%m%d')}_{counter}"
        if Path(f"{outdir}/{name}.zip").exists() or Path(f"{outdir}/{name}.gz").exists() \
                or Path(f"{outdir}/{name}.tar.gz").exists():
            counter += 1
        else:
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
    print(rf"Zip file created in {outdir}\{filename}.zip!")


def compress_to_gzip(indir, outdir, filename, extension='*') -> None:
    if indir.is_file():
        with tarfile.open(outdir / f'{filename}.tar.gz', 'w:gz') as tar_file:
            tar_file.add(indir, arcname=indir.relative_to(indir.parent))
            print(rf"Gzip file created in {outdir}\{filename}.tar.gz!")
    else:
        with tarfile.open(outdir / f'{filename}.tar.gz', 'w:gz') as tar_file:
            list_of_files = [file for file in indir.rglob(f'{extension}') if file.is_file()]
            for file in list_of_files:
                tar_file.add(file, arcname=file.relative_to(indir))
        print(rf"Gzip file created in {outdir}\{filename}.tar.gz!")


def compress_to_bzip2():
    print(" ")


def compress_to_xz():
    print("a")

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


def user_action() -> str:
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
            elif type_of_archive.lower() == "bzip2":
                return 'bzip2'
            elif type_of_archive.lower() == "xz":
                return 'xz'
            else:
                print("Invalid input. Please try again.")
                pass
        else:
            print("Invalid input. Please try again.")
            pass


def arg_parser():
    parser = argparse.ArgumentParser("Compress any file")
    compressing_group = parser.add_mutually_exclusive_group()
    compressing_group.add_argument('-z', '--zip-create',
                                   dest='zip_create',
                                   action='store_true', )
    compressing_group.add_argument('-g', '--gzip-create',
                                   help="Create a gzip file",
                                   dest='gzip_create',
                                   action='store_true')
    parser.add_argument('-i', '--indir',
                        help="Input directory",
                        dest='indir',
                        required=True)
    parser.add_argument('-o', '--outdir',
                        help="Output directory",
                        dest='outdir',
                        required=True)
    return parser.parse_args()


def main():
    if len(sys.argv) > 1:
        args = arg_parser()
        if args.zip_create:
            compress_to_zip(Path(args.indir), Path(args.outdir),
                            generate_archive_name(Path(args.indir), Path(args.outdir)))
        elif args.gzip_create:
            compress_to_gzip(Path(args.indir), Path(args.outdir),
                             generate_archive_name(Path(args.indir), Path(args.outdir)))
    else:
        while True:
            action = user_action()
            indir, outdir = ask_users_directory()
            if action == 'zip':
                compress_to_zip(indir, outdir, generate_archive_name(indir, outdir))
            elif action == 'gzip':
                compress_to_gzip(indir, outdir, generate_archive_name(indir, outdir))
            elif action == 'bzip2':
                compress_to_bzip2(indir, outdir, generate_archive_name(indir, outdir))
            elif action == 'xz':
                compress_to_xz(indir, outdir, generate_archive_name(indir, outdir))


if __name__ == '__main__':
    main()
