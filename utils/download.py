import sys
import math
import time
from os import path
import libtorrent as lt


class Downloader:
    def __init__(self, magnet) -> None:
        self.session = lt.session({"listen_interfaces": "0.0.0.0:6881"})
        self.info = lt.parse_magnet_uri(magnet)
        self.save_path = ""
        self.expanded_path = ""
        self.info.save_path = ""
    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_tuple = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_tuple[i])
    def get_path(self):
        try:
            self.save_path = input("\033[32;1m[+] enter the save path: \033[37m")
            if self.save_path.split() == []:
                print("\033[32;1m[+] Selecting default save path: \033[37m~/Downloads/")
                self.save_path = "~/Downloads/"
                self.expanded_path = path.expanduser(self.save_path)
            else:
                self.expanded_path = path.expanduser(self.save_path)
                return self.expanded_path

        except KeyboardInterrupt:
            print("\033[31;1m\n[~] exiting . . .\033[37m")
            sys.exit(0)

        except ValueError:
            print(
                "\033[33;1m[!] error detecting save path, going with defaults (path: ~/Downloads)\033[37m"
            )
            self.save_path = "~/Downloads/"
            self.expanded_path = path.expanduser(self.save_path)
            return self.expanded_path

        except TypeError:
            print(
                "\033[33;1m[!] error detecting save path, going with defaults (path: ~/Downloads)\033[37m"
            )
            self.save_path = "~/Downloads/"
            self.expanded_path = path.expanduser(self.save_path)
            return self.expanded_path
    def gen_download_stub(self):
        try:
            self.info.save_path = self.expanded_path
            session_card = self.session.add_torrent(self.info)
            download_stub = session_card.status()
            return download_stub
        except Exception:
            print(
                "\033[33;1m[!] error generating download stub, could not add magnet to session\033[37m"
            )

