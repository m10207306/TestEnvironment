# coding=utf8

import os
import cv2
import cfg
from Synthtext.gen import datagen, multiprocess_datagen
from Synthtext.random_factor import random_factor

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    
    text_surface_dir = os.path.join(cfg.output_dir, cfg.text_o_dir)
    bg_surface_dir = os.path.join(cfg.output_dir, cfg.bg_o_dir)
    comp_surface_dir = os.path.join(cfg.output_dir, cfg.comp_o_dir)
    
    makedirs(text_surface_dir)
    makedirs(bg_surface_dir)
    makedirs(comp_surface_dir)

    random_obj = random_factor()

    for idx in range(cfg.sample_num):
        text, font, font_size, bg, rotate_angle = random_obj.random()

        print (f"Generating step {idx + 1:>6d} / {cfg.sample_num:>6d}: text = {text:<20}, font = {font:20}, font_size = {font_size:3}, bg = {bg:25}, rotate_angle = {rotate_angle:20}")

    # mp_gen = multiprocess_datagen(cfg.process_num, cfg.data_capacity)
    # mp_gen.multiprocess_runningqueue()
    # digit_num = len(str(cfg.sample_num))

    # for idx in range(cfg.sample_num):
        # print ("Generating step {:>6d} / {:>6d}".format(idx + 1, cfg.sample_num))

        # t_s_list, bg_s_list, comp_s_list, text_list = mp_gen.dequeue_data()

        # i_t_path = os.path.join(i_t_dir, str(idx).zfill(digit_num) + '.png')
        
        # cv2.imwrite(i_t_path, i_t, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

    # mp_gen.terminate_pool()

if __name__ == '__main__':
    main()
