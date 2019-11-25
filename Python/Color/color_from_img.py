
'''
author: Pure Python
url: https://www.purepython.org
copyright: CC BY-NC 4.0
creation date: 20-12-2018
This script gets all colors from an image
and displays then in the terminal in rgb and hex values (with coloring!)
Just place your image or images in a folder.
Set the action for one or multiple (list) files
And run the script.
Sit back and relax
https://medium.com/purepython/get-colors-from-images-python-script-bd3fc47832ae
You need Pillow and Colr for this
https://python-pillow.org/
https://pypi.org/project/Colr/
Please install by :
pip install Pillow
pip install Colr
'''
from PIL import Image
from colr import Colr as C

class getColors:
    def __init__(self, files=None):
        if files is None:
            return None

        if type(files) is str:
            self.proces_image(files)
        else:
            for f in files:
                self.proces_image(f)

    def proces_image(self, image):
        colors = self.get_colors(image)
        seperator = '================================'
        print(C().b_rgb(0, 0, 0).rgb(255, 255, 255, seperator))
        print(C().b_rgb(0, 0, 0).rgb(255, 255, 255, image))
        print(C().b_rgb(0, 0, 0).rgb(255, 255, 255, seperator))
        for c in colors:
            self.show_colors(c[1])

    def get_colors(self, file):
        img = Image.open(file)
        return img.convert('RGB').getcolors()

    def show_colors(self, color):
        r = color[0]
        g = color[1]
        b = color[2]
        rgb = "rgb({}, {}, {}) | {}".format(r, g, b, self.rgb_to_hex(color))
        print(C().b_rgb(0, 0, 0).rgb(r, g, b, rgb))

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb


if __name__ == '__main__':
    # one file
    file = "/home/stable/Documents/Automation_SS/db/sql_test/Python/Color/data/image1.jpeg"
    # multiple files as list
    files = ['data/DNM65.png', 'data/color1.png', 'data/image1.jpeg']

    g = getColors(file)