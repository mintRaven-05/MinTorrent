import sys
import math
from requests import get
from tabulate import tabulate
from requests.utils import quote

class Magnet:
    def __init__(self) -> None:
        self.magnets = []
        self.table_header = [
            "Sl.No",
            "Seeders",
            "Leechers",
            "Name",
            "Size",
            "Category",
            "Info Hash",
        ]
        self.category_list = [
            "None",
            "audio",
            "video",
            "apps",
            "games",
            "nsfw",
            "other",
        ]
        self.trackers = [
            "http://104.28.1.30:8080/announce",
            "http://104.28.16.69/announce",
            "http://107.150.14.110:6969/announce",
            "http://109.121.134.121:1337/announce",
            "http://114.55.113.60:6969/announce",
            "http://125.227.35.196:6969/announce",
            "http://128.199.70.66:5944/announce",
            "http://157.7.202.64:8080/announce",
            "http://158.69.146.212:7777/announce",
            "http://173.254.204.71:1096/announce",
            "http://178.175.143.27/announce",
            "http://178.33.73.26:2710/announce",
            "http://182.176.139.129:6969/announce",
            "http://185.5.97.139:8089/announce",
            "http://188.165.253.109:1337/announce",
            "http://194.106.216.222/announce",
            "http://anidex.moe:6969/announce",
            "udp://tracker.openbittorrent.com:6969/announce",
            "udp://public.popcorn-tracker.org:6969/announce",
            "udp://9.rarbg.to:2710/announce",
            "upd://9.rarbg.me:2780/announce",
            "udp://9.rarbg.to:2730/announce",
            "udp://tracker.coppersurfer.tk:6969/announce",
            "udp://tracker.opentrackr.org:1337",
            "udp://tracker.torrent.eu.org:451/announce",
            "udp://tracker.tiny-vps.com:6969/announce"
            "udp://tracker.stealth.si:80/announce",
        ]
