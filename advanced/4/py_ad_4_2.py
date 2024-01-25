import glob
from PIL import Image


class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """_summary_

        Args:
            path_in (_type_, optional): _description_. Defaults to None.
            path_out (_type_, optional): _description_. Defaults to None.
            resize (tuple, optional): _description_. Defaults to (320,240).
        """
        self.path_in = path_in or "./*.png"
        self.path_out = path_out or "./output.gif"
        self.resize = resize

    def convert_gif(self):
        """_summary_"""
        print(self.path_in, self.path_out)  # logger추천
        img, *images = [
            Image.open(f).resize((320, 240), Image.ANTIALIAS)
            for f in sorted(glob.glob(self.path_in))
        ]
        try:
            img.save(
                fp=self.path_out,
                format="GIF",
                append_images=images,
                save_all=True,
                duration=500,
                loop=0,
            )
        except IOError:
            print(img)


if __name__ == "__main__":
    c = GifConverter()
    c.convert_gif
