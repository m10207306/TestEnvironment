
import os

import numpy as np

import cfg

class random_factor():

    def __init__(self):
        self.bg_dir = cfg.bg_dir
        self.font_dir = cfg.font_dir
        self.font_size_range = cfg.font_size
        self.char_txt = cfg.char_file
        self.char_maximum = cfg.char_maximum
        self.rotate_maximum = cfg.rotate_angle_max

        self.bg_list = os.listdir(self.bg_dir)
        self.font_list = os.listdir(self.font_dir)
        with open(self.char_txt, "r") as f:
            self.char_list = f.read().splitlines()
    
    def random(self):
        np.random.seed()

        ret_text = self.random_text()
        ret_font = np.random.choice(self.font_list)
        ret_font_size = np.random.randint(self.font_size_range[0], self.font_size_range[1] + 1)
        ret_bg = np.random.choice(self.bg_list)
        ret_rotate = np.random.rand() * self.rotate_maximum

        return ret_text, ret_font, ret_font_size, ret_bg, ret_rotate

    def random_text(self):
        ret_str = ""

        while len(ret_str) < self.char_maximum:
            if np.random.rand() < 0.3:
                ret_str += "\u3000"
            else:
                ret_str += np.random.choice(self.char_list)
        
        return ret_str