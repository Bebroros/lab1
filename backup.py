import compress
import decompress


def user_action():
    while True:
        action = input("Operation [d]ecompress or [c]ompress or [q]uit: ")
        if action.lower() == "c":
            compressor_to_use = input("Which compressor to use(zip, gzip, bzip2, xz): ")
            indir, outdir = compress.ask_users_directory()
            if compressor_to_use.lower() == "zip":
                compress.compress_to_zip(
                    indir, outdir, compress.generate_archive_name(indir, outdir)
                )
            elif compressor_to_use.lower() == "gzip":
                compress.compress_to_gzip(
                    indir, outdir, compress.generate_archive_name(indir, outdir)
                )
            elif compressor_to_use == "bzip2":
                compress.compress_to_bzip2(
                    indir, outdir, compress.generate_archive_name(indir, outdir)
                )
            elif compressor_to_use == "xz":
                compress.compress_to_xz(
                    indir, outdir, compress.generate_archive_name(indir, outdir)
                )
        elif action.lower() == "d":
            compressor_to_use = input(
                "Which decompressor to use(zip, gzip, bzip2, xz): "
            )
            indir, outdir = compress.ask_users_directory()
            if compressor_to_use.lower() == "zip":
                decompress.decompress_zip(indir, outdir)
            elif compressor_to_use.lower() == "gzip":
                decompress.decompress_gzip(indir, outdir)
            elif compressor_to_use == "bzip2":
                decompress.decompress_bzip2(indir, outdir)
            elif compressor_to_use == "xz":
                decompress.decompress_xz(indir, outdir)
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
