import argparse, sys

parser = argparse.ArgumentParser(
    prog = "booru-scraper", 
    description = "Downloads images from various booru websites using pybooru.",
    usage = "booru-scraper [options] -h",
    formatter_class = argparse.RawTextHelpFormatter,
    )

options = {
    parser.add_argument(
        "-t", 
        type = str,
        help = "Specify tags to filter images.",
        metavar = "TAGS",
    ),
    parser.add_argument(
        "-i",
        type = int,
        help = "Page number to start on. \n(Do not use with -c)",
        metavar = "INDEX"
    ),
    parser.add_argument(
        "-c",
        type = int,
        help = "Number of images to download. \n(Max is 50 images) (Do not use with -i)",
        default = 1,
        metavar = "COUNT"
    ),
    parser.add_argument(
        "-s",
        type = str,
        help = "Site used to download images from.",
        metavar = "SITE",
        default = "danbooru",
        choices = ["danbooru", "safebooru", "konachan", "yandere", "lolibooru"]
    ),

    parser.add_argument(
        "-p",
        type = str,
        help = "Path/directory to download images in. \nIf not specified, current working directory will be used.",
        metavar = "PATH" 
    ),
}

def get_conflict():
    args = parser.parse_args()

    if args.c and args.i is not None:
        print("Cannot use count and index together")
        sys.exit()

