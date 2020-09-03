from PIL import Image, ImageFilter
PATH = './img-processing/pics/'


def make_thumbnail_pic():
    thumbnail_img = Image.open(PATH + 'astro.jpg')
    thumbnail_img.thumbnail((450, 450))
    thumbnail_img.save(PATH + 'astro_thumbnail.jpg')
    return 0

def test_imgs():
    img = Image.open(PATH + 'pikachu.jpg')
    print(img.format == 'JPEG')
    filtered_img = img.filter(ImageFilter.SMOOTH)
    convert_img = img.convert('L')
    # png format support filters
    filtered_img.save(PATH + 'pikachu_smooth.png', 'png')
    convert_img.save(PATH + 'pikachu_grey.png', 'png')
    convert_img = convert_img.rotate(90)
    resize_img = convert_img.resize((300, 300))
    resize_img.show()
    return 0


def main():
    test_imgs()
    make_thumbnail_pic()
    return 0


if __name__ == "__main__":
    main()
