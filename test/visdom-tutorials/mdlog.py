import numpy as np
import cv2
import os


class mdlog:
    MAX_IM_WIDTH = 800

    def __init__(self, dump_dir=None):
        if dump_dir is None:
            dump_dir = "."
        self.dump_dir = dump_dir
        self.log_file = None

    def setup(self, log_file):
        self.log_file = self.dump_dir + os.sep + log_file
        if os.path.isfile(self.log_file) == True:
            os.remove(self.log_file)

    def image(self, im, im_fn, im_info):
        if self.log_file is None:
            return

        im_path = self.dump_dir + os.sep + im_fn
        cv2.imwrite(im_path, im)
        show_imgw = min(im.shape[1], self.MAX_IM_WIDTH)
        s = '<img src="{}" alt="x" style="width: {}px;"/>'.format(im_path, show_imgw)
        with open(self.log_file, 'a') as fp:
            fp.write(s + "\n")
            fp.write("cap:" + im_info + "\n")
            fp.close()

    def heading(self, text, level):
        level = min(level, 5)
        level = max(level, 0)
        if self.log_file is None:
            return
        with open(self.log_file, 'a') as fp:
            fp.write("{}{}\n".format("#" * level, text))
            fp.close()

    def info(self, text):
        with open(self.log_file, 'a') as fp:
            fp.write("{}\n".format(text))
            fp.close()

    def item(self, text):
        with open(self.log_file, 'a') as fp:
            fp.write("* {}\n".format(text))
            fp.close()

    def error(self, text):
        with open(self.log_file, 'a') as fp:
            fp.write("~~ERROR~~: {}\n".format(text))
            fp.close()


def markdownToHtml(html_path, md_path):
    os.system("pandoc -f markdown -t html -o {} {}".format(html_path, md_path))


if __name__ == "__main__":
    hl = mdlog()
    hl.setup("bat.md")
    hl.heading("hahaha1", level=1)
    hl.heading("hahaha2", level=2)
    hl.heading("hahaha3", level=3)
    hl.heading("hahaha3", level=3)
    hl.heading("hahaha3", level=3)
    hl.heading("hahaha3", level=3)

    im = np.zeros((100, 100), np.uint8)
    hl.image(im, im_fn='a.jpg', im_info="haha")

    hl.error("some bad")
    hl.info("ok ok")
