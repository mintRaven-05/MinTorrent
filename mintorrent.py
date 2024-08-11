import sys
import subprocess
from os import path
from tabulate import tabulate
from utils.magnet import Magnet
from utils.download import Downloader
from utils.torrent import Torrent

# ---------------------------------------------------------------------------------------------------
_TOOL_ = "MinTorrent"
_VERSION_ = "0.0.1"
_AUTHOR_ = "Debjeet Banerjee (mintRaven)"
_LICENSE_ = "GNU General Public License Version-3"
_COPYRIGHT_ = "Copyright (C) 2024, Debjeet Banerjee"
_DATE_ = "10th August, 2024"
_WEBSITE_ = "https://github.com/mintRaven-05"
# ---------------------------------------------------------------------------------------------------

try:
    flag = sys.argv[1]
    if flag == "-s" or flag == "--search":
        search_term_list = sys.argv[2:]
        search_term = " ".join(search_term_list)
        # ---------------------------------------------------------------------------------------------------
        if __name__ == "__main__":
            magnet = Magnet()
            try:
                results, magnet_list = magnet.search_magnets(search_term)
                magnet.print_magnet_match_table(results)

                choice = magnet.parse_option(len(magnet_list))
                try:
                    download = Downloader(magnet_list[choice])
                    download.get_path()
                    download.print_download_stub()
                except Exception:
                    print(
                        "\033[33;1m[!] error parsing your choice, going with defaults (option 1)\033[37m"
                    )
                    download = Downloader(magnet_list[0])
                    download.get_path()
                    download.print_download_stub()
                print()
            except KeyboardInterrupt:
                print()
            except Exception:
                print("\033[33;1m[!] error, no magnets found\033[37m")
        print()
    # ---------------------------------------------------------------------------------------------------
    elif flag == "-m" or flag == "--magnet":
        magnet_file_list = sys.argv[2:]
        magnet_file = " ".join(magnet_file_list)
        with open(magnet_file, "r") as file:
            magnet_text = file.readlines()[0]
        if __name__ == "__main__":
            magnet = Magnet()
            try:
                results, magnet_list = magnet.search_magnets(magnet_file)
                try:
                    download = Downloader(magnet_text)
                    download.get_path()
                    download.print_download_stub()
                except:
                    print()
            except KeyboardInterrupt:
                print()
            except Exception:
                print(
                    "\033[33;1m[!] error, make sure you have provided the correct file\033[37m"
                )
        print()
    # ---------------------------------------------------------------------------------------------------
    elif flag == "-t" or flag == "--torrent":
        torrent_file_list = sys.argv[2:]
        torrent_file = " ".join(torrent_file_list)
        if __name__ == "__main__":
            torrent = Torrent(torrent_file)
            try:
                torrent.get_path()
                torrent.print_download_stub()
            except:
                print(
                    "\033[33;1m[!] error, make sure you have provided the correct file\033[37m"
                )
        print()

    # ---------------------------------------------------------------------------------------------------
    elif flag == "-v" or flag == "--version":
        print(f"GNU {_TOOL_} v{_VERSION_}")
        print(f"{_COPYRIGHT_}")
        print(
            "This program is a free software; you may redistribute it under the terms of"
        )
        print(f"{_LICENSE_}")
        print(f"Written by {_AUTHOR_}, dated: {_DATE_}")
        print(f"visit {_WEBSITE_} for more projects")
    # ---------------------------------------------------------------------------------------------------
