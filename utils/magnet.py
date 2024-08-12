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
    def convert_size(self, size_bytes: int):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def gen_tracker_stub(self):
        self.trackers = [quote(tr) for tr in self.trackers]
        return "&tr=".join(self.trackers)

    def classify_category(self, category_id):
        category_id = int(category_id[0])
        category_id = category_id if category_id < len(self.category_list) - 1 else -1
        return self.category_list[category_id]

    def gen_magnet(self, info_hash, name):
        return f"magnet:?xt=urn:btih:{info_hash}&dn={quote(name)}&tr={self.gen_tracker_stub()}"
    def gen_match_table(self, results):
        index = 1
        max = 1
        match = []
        if results.status_code == 200:
            data = results.json()
            if data and "no results" in data[0]["name"].lower():
                return self.magnets
            for item in data:
                if max <= 20:
                    match.append(
                        [
                            index,
                            item["seeders"],
                            item["leechers"],
                            item["name"],
                            self.convert_size(int(item["size"])),
                            self.classify_category(item["category"]),
                            item["info_hash"],
                        ]
                    )
                    self.magnets.append(
                        self.gen_magnet(item["info_hash"], item["name"])
                    )
                    index += 1
                    max += 1
                else:
                    break
        return (match, self.magnets)
    def search_magnets(self, search_param: str):
        agent = "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
        url = f"https://apibay.org/q.php?q={quote(search_param)}"
        results = get(url, headers={"agent": agent})
        return self.gen_match_table(results)

    def print_magnet_match_table(self, magnet_list):
        print(
            tabulate(
                magnet_list,
                showindex=False,
                headers=self.table_header,
                tablefmt="simple",
                numalign="center",
            )
        )

    def parse_option(self, magnet_list_length):
        option = 0
        try:
            option = int(input("\n\033[32;1m[?] which magnet do you pick: \033[37m"))
            if option < 0 or option > magnet_list_length:
                print(
                    "\033[33;1m[!] error parsing option, going with defaults (option 1)\033[37m"
                )
                option = 0
                return option
            elif option > 0:
                option = option - 1
                return option
        except KeyboardInterrupt:
            print("\033[31;1m\n[~] exiting . . .\033[37m")
            sys.exit(0)
        except ValueError:
            print(
                "\033[33;1m[!] error parsing option, going with defaults (option 1)\033[37m"
            )
            option = 0
            return option
        except TypeError:
            print(
                "\033[33;1m[!] error parsing option, going with defaults (option 1)\033[37m"
            )
            option = 0
            return option
