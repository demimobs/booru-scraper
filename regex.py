from pybooru import Danbooru, Moebooru
import re

class Clients():

    def get_site(site):

        sites = { 
            "danbooru":   Danbooru('danbooru'),
            "yandere":    Moebooru('yandere'),
            "safebooru":  Moebooru('safebooru'),
            "konachan":   Moebooru('konachan'),
            "lolibooru":  Moebooru('lolibooru')
        }


        for i in sites.keys():
            if site == i:
                client = sites[i]
                return client
            else:
                pass

    def get_regex(site):

        sites = { 
            "danbooru":   r'https://cdn.donmai.us/original/[\w%._/-]+',
            "yandere":    r'https://files.yande.re/image/[\w%._/-]+',
            "konachan":   r'https://konachan.com/image/[\w%._/-]+',
            "lolibooru":  r'https://lolibooru.moe/image/[\(\)\s\w%._/-]+'
        }

        for i in sites.keys():
            if i == site:
                regex = sites[i]
                return regex
            else:
                pass
