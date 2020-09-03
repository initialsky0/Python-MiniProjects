import sys
from os import path, listdir, getcwd, makedirs
from PIL import Image

TEST_PATH = '\\img-processing\\pics\\'


def get_paths():
    # can improve by adding input validation
    cwd = path.abspath(getcwd())
    try:
        pics_path = cwd + TEST_PATH + sys.argv[1]
        new_path = cwd + TEST_PATH + sys.argv[2]
    except IndexError as err:
        print('Missing path argument')
        raise err

    return pics_path, new_path


def make_dir_exist(path_2_test):
    """ Return True if the directory exist or is created, and raise error if directory is not created """
    if not path.exists(path_2_test):
        try:
            # print('Create new dir')
            makedirs(path_2_test)
        except OSError as err:
            raise err
    return True


def convert_func(path_pic, path_new):
    imgs = listdir(path_pic)
    for img in imgs:
        img_path = f'{path_pic}\\{img}'
        # save_path = f"{path_new}\\{img.replace(img[-4:], '.png')}"
        save_path = f'{path_new}\\{path.splitext(img)[0]}.png'

        img_to_convert = Image.open(img_path)
        if img_to_convert.format == "JPEG":
            img_to_convert.save(save_path, 'png')
    return 0


def main():
    path_pic, path_new = get_paths()
    make_dir_exist(path_new)
    convert_func(path_pic, path_new)
    return 0


if __name__ == "__main__":
    main()
