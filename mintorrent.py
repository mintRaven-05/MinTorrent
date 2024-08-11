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

