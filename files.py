import os

def get_base_path(path, site):

    if path is None:
        base_dir = os.getcwd()
    else:
        base_dir = path

    image_path = base_dir + "/" + site
    
    if not os.path.isdir(image_path):
        os.mkdir(image_path)
        print("Making directory: " + image_path)
    else:
        print("Using already existing directory: " + image_path)
        pass

    return image_path