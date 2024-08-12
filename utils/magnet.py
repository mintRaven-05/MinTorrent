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
