from pathlib import Path
import zipfile
import tarfile
from compress import ask_users_directory
import argparse
import sys


def user_action():
    while True:
        action = input("Operation [d]ecompress or (q)uit: ")
        if action == "q":
            input("Press enter to quit")
            return quit()
        elif action == "d":
            kind_of_dec = input("Choose type of archive to decompress (zip/bzip2/xz/gzip): ")
            if kind_of_dec == "bzip2":
                return "bzip2"
            if kind_of_dec == "zip":
                return "zip"
            if kind_of_dec == "gzip":
                return "gzip"
            if kind_of_dec == "xz":
                return "xz"
        print("Invalid input. Please try again.")


def decompress_zip(source_file: Path, output_dir: Path):
    with zipfile.ZipFile(source_file, "r") as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Decompressed archive created in {output_dir}")


def decompress_xz(indir, outdir):
    with tarfile.open(indir, "r:xz") as tar:
        tar.extractall(outdir)
    print(f"Decompressed archive created in {outdir}")


def decompress_bzip2(source_file: Path, output_dir: Path):
    with tarfile.open(source_file, "r:bz2") as bz2_file:
        bz2_file.extractall(output_dir)
    print(f"Decompressed archive created in {output_dir}")


def decompress_gzip(indir, outdir):
    with tarfile.open(indir, "r:gz") as tar:
        tar.extractall(outdir)
    print(f"Decompressed archive created in {outdir}")


def arg_parser():
    parser = argparse.ArgumentParser("Decompress any file")
    compressing_group = parser.add_mutually_exclusive_group()
    compressing_group.add_argument('-z', '--zip-decompress',
                                   help="Decompress a zip file",
                                   dest='zip_decompress',
                                   action='store_true')
    compressing_group.add_argument('-b', '--bzip2-decompress',
                                   help="Decompress a bzip2 file",
                                   dest='bzip2_decompress',
                                   action='store_true')
    compressing_group.add_argument('-g', '--gzip-decompress',
                                   help="Decompress a gzip file",
                                   dest='gzip_decompress',
                                   action='store_true')
    compressing_group.add_argument('-x', '--xzip-decompress',
                                   help="Decompress a xzip file",
                                   dest='xzip_decompress',
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
        if args.zip_decompress:
            decompress_zip(args.indir, args.outdir)
        if args.gzip_decompress:
            decompress_gzip(args.indir, args.outdir)
        elif args.bzip2_decompress:
            decompress_bzip2(args.indir, args.outdir)
        elif args.gzip_decompress:
            decompress_gzip(args.indir, args.outdir)
        elif args.xzip_decompress:
            decompress_xz(args.indir, args.outdir)
    else:
        while True:
            action = user_action()
            source_file, output_dir = ask_users_directory()
            if action == "zip":
                decompress_zip(source_file, output_dir)
            if action == "bzip2":
                decompress_bzip2(source_file, output_dir)
            if action == "gzip":
                decompress_gzip(source_file, output_dir)
            if action == "xz":
                decompress_xz(source_file, output_dir)


if __name__ == "__main__":
    main()
