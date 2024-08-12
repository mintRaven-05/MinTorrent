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
    
