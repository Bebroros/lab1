from pathlib import Path
import zipfile
import bz2
import tarfile
from compress import ask_users_directory


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
    with zipfile.ZipFile(source_file, "r") as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Decompressed archive created in {output_dir}")


def decompress_xz(indir, outdir):
    with tarfile.open(indir, "r:xz") as tar:
        tar.extractall(outdir)
    print(f"Decompressed archive created in {outdir}")


def decompress_bzip2(source_file: Path, output_dir: Path):
    output_file = output_dir / source_file.name.replace(".bz2", "")
    with open(source_file, "rb") as input_file:
        decompressed_file = bz2.decompress(input_file.read())
    with open(output_file, "wb") as output_file:
        output_file.write(decompressed_file)
    print(f"Decompressed archive created in {output_dir}")


def decompress_gzip(indir, outdir):
    with tarfile.open(indir, "r:gz") as tar:
        tar.extractall(outdir)
    print(f"Decompressed archive created in {outdir}")


def main():
    action = user_action()
    source_file, output_dir = ask_users_directory()
    if action == "zip":
        decompress_zip(source_file, output_dir)
    if action == "bzip2":
        decompress_bzip2(source_file, output_dir)
    if action == "gzip":
        decompress_gzip(source_file, output_dir)


if __name__ == "__main__":
    main()
