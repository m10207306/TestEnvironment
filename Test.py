# import xlrd, sys, copy, random
# import matplotlib.pyplot as plt
# import numpy as np

# import AccuracyPlot

# ------- Plot Accuracy -------
# myworkbook = xlrd.open_workbook('/Users/garyliang/Downloads/AccuracyData.xlsx')
# sheet0 = myworkbook.sheet_by_index(0)
# nrows = sheet0.nrows
# ncols = sheet0.ncols
# TC_Ref = tuple(sheet0.col_values(0))
# TC_Val = tuple(sheet0.col_values(1))
# TG_Ref = sheet0.col_values(2)
# TG_Val = sheet0.col_values(3)
# HDL_Ref = sheet0.col_values(4)
# HDL_Val = sheet0.col_values(5)
#
# TG_Ref = tuple(x for x in TG_Ref if x != '')
# TG_Val = tuple(x for x in TG_Val if x != '')
# HDL_Ref = tuple(x for x in HDL_Ref if x != '')
# HDL_Val = tuple(x for x in HDL_Val if x != '')
#
# AccuracyPlot.accuracy_plot(TC_Ref, TC_Val, 'TC Accuracy Evaluation', 'Cobas c111(mg/dL)',
#                            'PixoTest POCT System(mg/dL)', 20, '/Users/garyliang/Downloads/Test_TC.png')
# AccuracyPlot.accuracy_plot(TG_Ref, TG_Val, 'TG Accuracy Evaluation', 'Cobas c111(mg/dL)',
#                            'PixoTest POCT System(mg/dL)', 20, '/Users/garyliang/Downloads/Test_TG.png')
# AccuracyPlot.accuracy_plot(HDL_Ref, HDL_Val, 'HDL Accuracy Evaluation', 'Cobas c111(mg/dL)',
#                            'PixoTest POCT System(mg/dL)', 15, '/Users/garyliang/Downloads/Test_HDL.png')

# Slice範例
# letters = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# print(letters[0:3:1])
# print(letters[0:5:2])
# print('')
# print(letters[::1])
# print(letters[0:len(letters):1])
# print('')
# print(letters[::-1])
# print(letters[-1:-len(letters)-1:-1])


# Zip功能
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = [(1, 2), (3, 4), (5, 6)]
#
# zipped1 = zip(a, b)
# zipped2 = copy.deepcopy(zipped1)
#
# x, y = zip(*zipped2)
# print(x, y)
#
# x, y = zip(*d)
# print(x, y)
#
# for i in zipped1:
#     print(i)
# else:
#     print("finish for loop or no content in zipped1")
#
# for i in zipped2:   # 無內容（原因待確認）
#     print(i)
# else:
#     print("finish for loop or no content in zipped2")


# 列表解析式 List Comprehension
# your_list = [[[] for x in range(9)] for y in range(10)]
# print(len(your_list))
# print(len(your_list[0]))


# Default Parameter
# def buggy(arg, result = []):
#     result.append(arg)
#     print(result)
#
# buggy('a')
# buggy('b')
#
# list1 = []
# buggy('a', list1)
# list2 = []
# buggy('b', list2)


# Docstring
# def test(a):
#     "Test for doc string"   # documentation of the function
#     print(a)
#
# help(test)


# Inner Functions (Closures)
# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#     return inner2
#
# a = knights2("Duck")
# b = knights2("Hasenpfeffer")
#
# print(a())
# print(b())


# Lambda Function - 常用於GUI的Callback functions
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
#
# edit_story(stairs, lambda word:word.capitalize() + '!')


# Generators
# generator1 = range(1, 100)  # 產生generator
# print(generator1)
#
# def userdef_range(first = 0, last = 10, step = 1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# generator2 = userdef_range(1, 5)    # user define generator
# print(generator2)
# for x in generator2:
#     print(x)


# Decorators 裝飾器
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function
#
# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function
#
# def add_int1(a, b):
#     return a + b
#
# # 原始方法
# cooler_add_ints = document_it(add_int1)
# cooler_add_ints(3, 5)
# # 裝飾器標準方法
# @document_it
# def add_int1(a, b):
#     return a + b
# add_int1(3, 5)
#
# # 多重裝飾器（測試不同順序）
# @square_it
# @document_it
# def add_int1(a, b):
#     return a + b
# add_int1(3, 5)
#
# @document_it
# @square_it
# def add_int1(a, b):
#     return a + b
# add_int1(3, 5)


# Namespace and Scope
# animal = "fruitbat"
# def change_and_print_global():
#     global animal
#     animal = "wombat"
#     print("inside change_and_print_global:", animal)
#
# print(animal)
# change_and_print_global()
# print(animal)
#
# animal = "fruitbat"     # locals() and globals()
# def change_local():
#     animal = "wombat"
#     print("locals:", locals())
#
# print("globals:", globals())


# Try and Except
# short_list = [1, 2, 3]
# position = 5
# try:
#     short_list[position]
# except:
#     print('Need a position between 0 and', len(short_list)-1, ' but got', position)


# 當收到特定Exception時做特定動作
# short_list = [1, 2, 3]  # provide a separate exception handler
# while True:
#     value = input("Position [q to quit]?")
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else broke:', other)


# setdefault 為特定的key設定default值
# periodic_table = {'Hydrogen': 1, 'Helium': 2}
# carbon = periodic_table.setdefault('Carbon', 12)
# print(periodic_table)
# helium = periodic_table.setdefault('Helium', 947)
# print(periodic_table)


# defaultdict 創造一個所有key都可以在該type上有預設值的dict
# from collections import defaultdict
# periodic_table = defaultdict(int)
# periodic_table['Hydrogen'] = 1
# print(periodic_table['Lead'])  # 原本不存在的key，但是有預設值


# deque = stack + queue
# def palindrome(word):               # 如果輸入的內容長度>1，且最左邊不等於最右邊則return false，除此之外return true
#     from collections import deque
#     dq = deque(word)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#     return True
#
# palindrome('')  # True
# palindrome('racecar')   # True
# palindrome('halibut')   # False


# itertools
# import itertools
# for item in itertools.chain([1, 2], ['a', 'b']):    # chain 把兩個input的內容當成一個來iterate
#     print(item)
#
# for item in itertools.cycle([1, 2]):                # cycle 循環iterate
#     print(item)
#
# for item in itertools.accumulate([1, 2, 3, 4]):     # calculates accumulate (default usage)
#     print(item)
#
# def multiply(a, b):
#     return a * b
#
# for item in itertools.accumulate([1, 2, 3, 4], multiply):   # accumulated product
#     print(item)


# pretty printer
# from pprint import pprint
# from collections import OrderedDict
# quotes = OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!'), ])
# print(quotes)
# pprint(quotes)  # 可讀性較好的print


# Class - 用properties不讓變數可以被直接存取或變動(事實上還是可以直接存取)
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)
#
# fowl = Duck('Howard')
# print(fowl.name)
# print(fowl.get_name())
# fowl.name = 'Daffy'
# print(fowl.name)

# Class -
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#
# fowl = Duck('Howard')
# fowl.name
# fowl.name = 'Donald'
# fowl.name

######### plotly
# import plotly.graph_objects as go
#
# fig = go.Figure()
# fig.update_xaxes(range = [0, 5], title_text = "xlabel")#, showgrid = True, gridwidth = 1, gridcolor = "rgba(0, 0, 0, 0.1)")
# fig.update_yaxes(range = [0, 5], title_text = "ylabel")#, showgrid = True, gridwidth = 1, gridcolor = "rgba(0, 0, 0, 0.1)")
#
# font_family = "Times New Roman"
# fig.update_layout(showlegend = False, title = dict(text = "Accuracy Plot Clinical Data PixoHealth Cobas <br> Bias = 100% <br>" + font_family, x = 0.5),
#                   annotations = [dict(x = 5*0.1, y = 5*0.9, text = "Y = a x + b", showarrow = False)],
#                   font = dict(size = 18, family = font_family)) #plot_bgcolor = "rgba(0, 0, 0, 0)")
#
# fig.add_scatter(x = [1, 2, 3], y = [1, 2, 3], mode = "markers", marker = dict(size = 15, color = "rgba(0, 0, 0, 0)", line = dict(width = 2, color = "rgba(255, 0, 0, 0.5)")))
#
# fig.add_scatter(x = [1, 2, 3], y = [1, 2, 3], mode = "lines", line = dict(width = 2, color = "rgba(255, 0, 0, 0.5)", dash = "dash"))
#
#
#
# fig.show()



# def plti(img, **kwargs):
#     fig, ax = plt.subplots(1, 1)
#     ax.imshow(img, **kwargs)
#     return fig, ax
#
#
# img = plt.imread("/Users/garyliang/PyCharm/Test/IMG_20190823_174302_Glass_1280720.png")
#
# print("Img1 Shape = ", img.shape)
# img = (img * 255).astype("int")
# # fig1, ax1 = plti(img)
# # ax1.axvline(x = 360, color = "r")
# # ax1.axhline(y = 640, color = "r")
#
# img2 = img[639-480:639+480, 359-270:359+270, :]
# print("Img2 Shape = ", img2.shape)
# fig2, ax2 = plti(img2)
# ax2.axvline(x = 271, color = "r", label = "Vertical Line")
# ax2.axhline(y = 481, color = "b", label = "Horizontal Line")
#
# handles, labels = ax2.get_legend_handles_labels()
# ax2.legend(handles, labels)
# # 如果想要把legend放在外面
# # ax.legend([handle1, handle2])  就直接以handel自己本身的label去legend
# # ax.legend([handle1, handle2, handle3], [label1, label2, label3])
# ax2.legend(bbox_to_anchor = (1, 1))
#
# x_row, y_col = 480, 270
# color = ["r", "g", "b"]
# fig3, ax3 = plt.subplots(1, 1)
# for i in range(3):
#     tmp_mat = img2[x_row, :, i].flatten()
#     tmp_mat = tmp_mat / max(tmp_mat)
#     ax3.plot(tmp_mat, color = color[i], label = color[i], linewidth = 0.5)
# ax3.grid(alpha = 0.5)
# ax3.legend(bbox_to_anchor = (1, 1))
# ax3.set_title("Horizontal Profile")
# ax3.set_xlabel("Pixel")
# ax3.set_ylabel("Signal Ratio")

# fig4, ax4 = plt.subplots(1, 1)
# for i in range(3):
#     tmp_mat = img2[:, y_col, i].flatten()
#     tmp_mat = tmp_mat / max(tmp_mat)
#     ax4.plot(tmp_mat, color = color[i], label = color[i], linewidth = 0.5)
# ax4.grid(alpha = 0.5)
# ax4.legend(bbox_to_anchor = (1, 1))
# ax4.set_title("Vertical Profile")
# ax4.set_xlabel("Pixel")
# ax4.set_ylabel("Signal Ratio")

# plt.ion()
#
# x_arr, y_arr = np.meshgrid(np.array(range(540)), np.array(range(960)))
# # fig5, ax5 = plt.subplots(1, 1, projection = "3d")   # 不能用，因為subplots沒有projection的kw，因此只能如下，分兩步做
# fig5 = plt.figure()
# from mpl_toolkits.mplot3d import Axes3D
# ax5 = fig5.add_subplot(111, projection = "3d")        # 111 = row1 col1 number1
#
# surf_handle = ax5.plot_surface(x_arr, y_arr, img2[:, :, 1], cmap = "rainbow")
# fig5.colorbar(surf_handle, shrink = 0.7, ticks = range(0, 255, 25))    # shrink設定colorbar長度，aspect設定寬度
#
# plt.show()
#
# ax5.view_init(30, -30)
# plt.draw()
#
# ax5.view_init(30, -60)
# plt.draw()

# 暫時找不到可以Iterately轉角度的辦法，嘗試過FuncAnimation、plt.pause(.1)等，皆無法
# 另外發現Preference->Tools->PythonScientific->取消Show Plot in Tool Box比較好用



# import keyboard
#
# def detect(callback):
#     print(callback.name)
#
# keyboard.hook(detect)
# keyboard.wait()
#
# while True:
#     print(keyboard.is_pressed("a"))


# import pygame, time
# pygame.init()
# screen = pygame.display.set_mode((600, 400))    # window size
# pygame.display.set_caption("Control Window")    # window title
# screen.fill((0, 0, 0))                          # window background color
# pygame.display.update()                         # update window color (maybe including other setting)
# font = pygame.font.Font(None, 50)               # create a new font object from a file (*args = filename, size)
#
# temp_text = ""
# input_text = ""
# enter = False
# while True:
#     time.sleep(0.1)                             # 10 frames/sec
#     # ============================================ Keyboard Detection
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.unicode.isalpha():
#                 temp_text += event.unicode
#             elif event.key == pygame.K_BACKSPACE:
#                 temp_text = temp_text[:-1]
#             elif event.key == pygame.K_RETURN:
#                 input_text = temp_text
#                 temp_text = ""
#                 enter = True
#         elif event.type == pygame.QUIT:
#             enter = True
#     # ============================================
#     if not enter:
#         rendered_text = font.render(temp_text, True, (255, 255, 255))
#         rect = rendered_text.get_rect()
#         screen.blit(rendered_text, rect)
#         pygame.display.flip()
#     else:
#         screen.fill((0, 0, 0))
#         pygame.display.update()
#         enter = False
#
# print("Text from pygame input: " + input_text)


# ================================ Sample for updated print
# def update_print(content):
#     sys.stdout.write("\r>> " + content)
#     sys.stdout.flush()

# ================================ Don't use convert_alpha()
# import os
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"   # Block the information from importing pygame
# import pygame
#
# width = 1024
# height = 768
# Black = (0, 0, 0)
#
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# black_window = pygame.Surface((width, height)).convert()
# black_window.fill(Black)
#
# # bg = pygame.Surface(screen.get_size())
# img = pygame.image.load(os.path.join("..", "Ragnarok", "BG_Image", "Login_BG.png")).convert()
# # pygame.transform.scale(img, screen.get_size(), bg)
#
# alpha = 0
# step = 5
# while True:
#     pygame.time.Clock().tick(30)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:  # reset current cmd and clear block
#                 pygame.quit()
#     if alpha < 0:
#         step = 5
#     elif alpha > 250:
#         step = -5
#     alpha += step
#     img.set_alpha(alpha)
#     screen.blit(black_window, (0, 0))
#     screen.blit(img, (0, 0))
#     pygame.display.update()

# import os
# import DirectoryTool
#
# root_path = "/Volumes/Ixensor/01.研發部（RDD）/軟體演算組（ALG）/Experiment_Data/Lipid/20190430_IDT_RawData_Gary"
#
# Meter_list = DirectoryTool.tool_spec_name_folder(root_path, "No.")
#
# for meter in Meter_list:
#     Exp_list = DirectoryTool.tool_spec_name_folder(meter, "M_Lip")
#     print(meter)
#     for data in Exp_list:
#         print("  ", os.path.join(meter, data))
#         Img_list = DirectoryTool.tool_spec_ext_file(os.path.join(meter, data), "jpeg")
#         for jpg in Img_list:
#             print("    ", os.path.join(meter, data, jpg))


# import os
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"   # Block the information from importing pygame
# import pygame                                       # 3rd party Library
# import math
#
#
# class character(pygame.sprite.Sprite):
#
#     def __init__(self, standby_image_path, attack_image_path):
#         super().__init__()
#         self.standby_image = pygame.image.load(standby_image_path).convert()
#         self.standby_image.set_colorkey((255, 0, 255))
#         self.standby_animate_num = self.standby_image.get_size()[0] / 200
#         self.attack_image = pygame.image.load(attack_image_path).convert()
#         self.attack_image.set_colorkey((255, 0, 255))
#         self.attack_image_num = self.attack_image.get_size()[0] / 200
#         self.current = 0
#         self.status_idx = 0
#         self.image = []
#         self.rect = []
#
#     def update(self, switch):
#         img_list = [self.standby_image, self.attack_image]
#         if switch:
#             self.status_idx = abs(self.status_idx - 1)
#             self.current = 0
#         if self.current == self.standby_animate_num:
#             self.current = 0
#         self.current += 1
#         self.image = img_list[self.status_idx].subsurface(pygame.Rect((self.current-1) * 200, 0, 200, 200))
#         self.rect = self.image.get_rect()
#         self.rect.x = 1024 * 0.4 - self.rect.width / 2
#         self.rect.y = 768 * 0.55 - self.rect.height / 2
#
#
# pygame.init()
# Clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1024, 768))
#
# playerGroup = pygame.sprite.Group()
# playerGroup.add(character(os.path.join("..", "Ragnarok", "Char_Image", "Novice", "Standby_Dagger.png"),
#                           os.path.join("..", "Ragnarok", "Char_Image", "Novice", "Attack_Dagger.png")))
#
# bg = pygame.image.load(os.path.join("..", "Ragnarok", "BG_Image", "Battle.png")).convert()
# screen.blit(bg, (0, 0))
# switch = False
#
# while True:
#     Clock.tick(10)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_e:
#                 pygame.quit()
#             elif event.key == pygame.K_a:
#                 switch = not switch
#
#     # standby = 1 frame
#     # attack = 2 frame
#     playerGroup.clear(screen, bg)
#     playerGroup.update(switch)
#     playerGroup.draw(screen)
#     pygame.display.update()
#     if switch:
#         switch = not switch


# import os, datetime
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"   # Block the information from importing pygame
# import pygame                                       # 3rd party Library
#
# pygame.init()
# Clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1024, 768))
#
# bg = pygame.image.load(os.path.join("..", "Ragnarok", "BG_Image", "Battle.png")).convert()
# # screen.blit(bg, (0, 0))
#
# bg2 = bg.subsurface(pygame.Rect(0, 0, 100, 100))
#
# class character(pygame.sprite.Sprite):
#     def __init__(self, path):
#         super().__init__()
#         self.image = []
#         self.rect = []
#         self.ori_image = pygame.image.load(path).convert()
#         self.ori_image.set_colorkey(self.ori_image.get_at((0, 0)))
#         self.idx = 0
#         self.width = 200
#
#     def update(self):
#         if self.idx == 6:
#             self.idx = 0
#         self.idx += 1
#         self.image = self.ori_image.subsurface(pygame.Rect((self.idx - 1) * self.width, 0, self.width, self.width))
#         self.rect = self.image.get_rect()
#
# playerGroup = pygame.sprite.Group()
# playerGroup.add(character(os.path.join("..", "Ragnarok", "Char_Image", "Novice", "Attack_Dagger_test.png")))
#
# while True:
#     current = datetime.datetime.now()
#     Clock.tick(60)
#     print(Clock.get_fps())
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_e:
#                 pygame.quit()
#     print(datetime.datetime.now() - current)
#     current = datetime.datetime.now()
#
#     playerGroup.clear(screen, bg)
#     print(" ", datetime.datetime.now() - current)
#     current = datetime.datetime.now()
#
#     playerGroup.update()
#     print("  ", datetime.datetime.now() - current)
#     current = datetime.datetime.now()
#
#     playerGroup.draw(screen)
#     print("   ", datetime.datetime.now() - current)
#     current = datetime.datetime.now()
#
#     pygame.display.update(pygame.Rect(0, 0, 200, 200))
#     print("    ", datetime.datetime.now() - current)
#     current = datetime.datetime.now()


# 有順序的group，可以用在傷害數字上，測試起來是塞了89個東西要blit之後才開始掉frame(以60fps來算)
import os, random
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"   # Block the information from importing pygame
import pygame                                       # 3rd party Library


pygame.init()
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
all_damage = pygame.image.load(os.path.join("..", "Ragnarok-Idle-Game", "Info_Image", "Damage.png")).convert()
all_damage.set_colorkey(all_damage.get_at((0, 0)))
damage_list = []
for i in range(0, 10):
    damage_list.append(all_damage.subsurface(pygame.Rect(i*10, 0, 10, 13)))
cri_image = pygame.image.load(os.path.join("..", "Ragnarok-Idle-Game", "Info_Image", "Critical.png")).convert()
cri_image.set_colorkey(cri_image.get_at((0, 0)))
miss_image = pygame.image.load(os.path.join("..", "Ragnarok-Idle-Game", "Info_Image", "Miss.png")).convert()
miss_image.set_colorkey(miss_image.get_at((0, 0)))


class Damage(pygame.sprite.Sprite):
    AllGroup = []

    def __init__(self, damage1, type1):
        super().__init__()
        damage_value = [int(d) for d in str(damage1)]
        self.image = pygame.Surface((70, 60)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        if type1 == 1 or type1 == 3:
            if type1 == 1:
                self.image.blit(cri_image, (0, 0))
            damage_surface = pygame.Surface((10 * len(damage_value), 13)).convert()
            damage_surface.set_colorkey((0, 0, 0))
            for i in range(0, len(damage_value)):
                damage_surface.blit(damage_list[damage_value[i]], (i * 10, 0))
            rect = damage_surface.get_rect()
            rect.center = self.rect.center
            self.image.blit(damage_surface, rect)
        elif type1 == 2:
            rect = miss_image.get_rect()
            rect.center = self.rect.center
            self.image.blit(miss_image, rect)

        self.life = 0

    def update(self):
        if self.life >= 40:
            Damage.AllGroup.remove(self)
        else:
            self.life += 1
        self.rect.x += 2
        self.rect.y += 2


playerGroup = pygame.sprite.Group()
Damage.AllGroup = playerGroup

bg = pygame.image.load(os.path.join("..", "Ragnarok-Idle-Game", "BG_Image", "Battle.png")).convert()
screen.blit(bg, (0, 0))

count = 1
while True:
    Clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    if count % 10 == 0:
        type_ = random.randint(1, 3)
        damage = random.randint(10, 10000)
        playerGroup.add(Damage(damage, type_))
    playerGroup.clear(screen, bg)
    playerGroup.update()
    playerGroup.draw(screen)
    pygame.display.update()

    count += 1





