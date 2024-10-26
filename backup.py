import argparse
import sys
from pathlib import Path
import compress
import decompress


def get_extension(indir):
    if indir.is_dir():
        extensions = input("Enter what extensions you to compress:")
        if extensions == "":
            return None
        extensions = extensions.split()
        return extensions
    else:
        return None


def arg_parser():
    parser = argparse.ArgumentParser("Compress or decompress any file")
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('-c', '--compress',
                              help="Compress a file",
                              dest='compress',
                              action='store_true')
    action_group.add_argument('-d', '--decompress',
                              help="Decompress a file",
                              dest='decompress',
                              action='store_true')
    compressing_group = parser.add_mutually_exclusive_group()
    compressing_group.add_argument('-z', '--zip',
                                   help="Compress a zip file",
                                   dest='zip',
                                   action='store_true')
    compressing_group.add_argument('-g', '--gzip',
                                   help="Create a gzip file",
                                   dest='gzip',
                                   action='store_true')
    compressing_group.add_argument('-b', '--bzip2',
                                   help="Create a bzip2 file",
                                   dest='bzip2',
                                   action='store_true')
    compressing_group.add_argument('-x', '--xzip',
                                   help="Create a xzip file",
                                   dest='xzip',
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


def user_action():
    while True:
        action = input("Operation [d]ecompress or [c]ompress or [q]uit: ")
        if action.lower() == "c":
            compressor_to_use = input("Which compressor to use(zip, gzip, bzip2, xz): ")
            if compressor_to_use.lower() == "zip":
                indir, outdir = compress.ask_users_directory()
                compress.compress_to_zip(
                    indir, outdir, compress.generate_archive_name(indir, outdir),
                    get_extension(indir)
                )
            elif compressor_to_use.lower() == "gzip":
                indir, outdir = compress.ask_users_directory()
                compress.compress_to_gzip(
                    indir, outdir, compress.generate_archive_name(indir, outdir),
                    get_extension(indir)
                )
            elif compressor_to_use == "bzip2":
                indir, outdir = compress.ask_users_directory()
                compress.compress_to_bzip2(
                    indir, outdir, compress.generate_archive_name(indir, outdir),
                    get_extension(indir)
                )
            elif compressor_to_use == "xz":
                indir, outdir = compress.ask_users_directory()
                compress.compress_to_xz(
                    indir, outdir, compress.generate_archive_name(indir, outdir),
                    get_extension(indir)
                )
            else:
                print("Invalid input. Please try again.")
                pass
        elif action.lower() == "d":
            compressor_to_use = input(
                "Which decompressor to use(zip, gzip, bzip2, xz): "
            )
            if compressor_to_use.lower() == "zip":
                indir, outdir = compress.ask_users_directory()
                decompress.decompress_zip(indir, outdir)
            elif compressor_to_use.lower() == "gzip":
                indir, outdir = compress.ask_users_directory()
                decompress.decompress_gzip(indir, outdir)
            elif compressor_to_use == "bzip2":
                indir, outdir = compress.ask_users_directory()
                decompress.decompress_bzip2(indir, outdir)
            elif compressor_to_use == "xz":
                indir, outdir = compress.ask_users_directory()
                decompress.decompress_xz(indir, outdir)
            else:
                print("Invalid input. Please try again.")
                pass
        elif action.lower() == "q":
            print("Thank you!")
            input("Press enter to exit")
            quit()
        else:
            print("Invalid input. Please try again.")


def main():
    if len(sys.argv) > 1:
        args = arg_parser()
        if args.compress:
            if args.zip:
                compress.compress_to_zip(
                    Path(args.indir), Path(args.outdir),
                    compress.generate_archive_name(Path(args.indir), Path(args.outdir)),
                    get_extension(Path(args.indir))
                )
            elif args.gzip:
                compress.compress_to_gzip(
                    Path(args.indir), Path(args.outdir),
                    compress.generate_archive_name(Path(args.indir), Path(args.outdir)),
                )
            elif args.bzip2:
                compress.compress_to_bzip2(
                    Path(args.indir), Path(args.outdir),
                    compress.generate_archive_name(Path(args.indir), Path(args.outdir))
                )
            elif args.xzip:
                compress.compress_to_xz(
                    Path(args.indir), Path(args.outdir),
                    compress.generate_archive_name(Path(args.indir), Path(args.outdir))
                )
        elif args.decompress:
            if args.zip:
                decompress.decompress_zip(Path(args.indir), Path(args.outdir))
            if args.gzip:
                decompress.decompress_gzip(Path(args.indir), Path(args.outdir))
            if args.bzip2:
                decompress.decompress_bzip2(Path(args.indir), Path(args.outdir))
            if args.xzip:
                decompress.decompress_xz(Path(args.indir), Path(args.outdir))
    else:
        user_action()


if __name__ == "__main__":
    main()
