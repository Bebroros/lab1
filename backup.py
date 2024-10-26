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
    user_action()


if __name__ == "__main__":
    main()
