import re, os
import urllib.request as req

import regex, kargs, files

info = vars(kargs.parser.parse_args())

tags  = info["t"]
index = info["i"]
count = info["c"]
site  = info["s"]
path  = info["p"]

client = regex.Clients.get_site(site)
link_regex = regex.Clients.get_regex(site)

def get_image_url(post_limit, page_index, image_tags):
    image_data = client.post_list(limit = post_limit, page = page_index, tags = image_tags)
    url_search = re.compile(link_regex)
    url_results = set(url_search.findall(str(image_data)))
    return url_results

def download_images(num, page, tags, path, site):
    urls = get_image_url(num, page, tags)
    save_path = files.get_base_path(path, site)

    if os.path.isdir(save_path):
        pass
    else:
        os.mkdir(save_path)

    for i in urls:
        kargs.get_conflict()
        url_path, image_file = os.path.split(i)
        req.urlretrieve(str(i), save_path + "/" + image_file)
        print('Downloading ' + i + " into " + save_path)

def message():
    kargs.parser.print_usage()
    print("-t: Specify tags to filter images")
    print("-h: Show help")

def stdout():
    if tags is None:
        message()
    else:
        download_images(count, index, tags, path, site)

stdout()