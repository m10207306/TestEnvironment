#   ref_list, data_list : python list container
#   title_str, xlabel_str, ylabel_str : string
#   bias : double
#   save_path = /xxx/xxx/xxx/xxx/file_name.png
#   if you don't want to save image, set the save_path to empty string

import matplotlib.pyplot as plt
import numpy as np


def accuracy_plot(ref_list, data_list, title_str, xlabel_str, ylabel_str, bias, save_path = ''):
    boundary = max(ref_list + data_list)
    if boundary <= 15:                          # A1C Case
        boundary = 15.
        tick_step = 1.
    elif 15 < boundary <= 110:                  # HDL Case
        boundary = 110.
        tick_step = 10.
    elif boundary > 110:                        # TC, TG Case
        boundary = ((boundary // 100.) + 1) * 100.
        tick_step = 50.
    else:                                       # Exception Case
        boundary = 1000.
        tick_step = 50.

    if boundary >= 100:
        thres_x = [0., 100., boundary]
        thres_y1 = np.array([0. + bias, 100. + bias, boundary * (1 + bias / 100.)])
        thres_y2 = np.array([0. - bias, 100. - bias, boundary * (1 - bias / 100.)])
    else:
        thres_x = np.array([0., boundary])
        thres_y1 = np.array([0. + bias, boundary + bias])
        thres_y2 = np.array([0. - bias, boundary - bias])

    #   Figure Setting
    fig, axes = plt.subplots(1, 1)
    axes.set_xlim(0, boundary)
    axes.set_ylim(0, boundary)
    axes.set_xticks(np.arange(0, boundary+1, tick_step))
    axes.set_yticks(np.arange(0, boundary+1, tick_step))
    axes.grid(color = 'k', linestyle = '--', alpha = 0.2)
    axes.set_xlabel(xlabel_str)
    axes.set_ylabel(ylabel_str)

    #   Analysis Outlier
    ref = np.array(ref_list)
    data = np.array(data_list)
    index = ref > 100
    index2 = np.invert(index)
    thres_list = ref.copy()
    thres_list[index] = thres_list[index] * bias / 100.0
    thres_list[index2] = bias
    bias_list = abs(data - ref)
    outlier_index = bias_list > thres_list
    acc = ( bias_list.size - np.sum(outlier_index) ) / bias_list.size

    fitting_coe = np.polyfit(ref, data, 1)
    regression = np.poly1d(fitting_coe)

    R = np.corrcoef(ref, data)[0, 1]
    R_Square = R * R



    #   Plot and Config
    sc1 = axes.scatter(ref[outlier_index], data[outlier_index], marker = 'o', color = 'r', s = 25, label = 'Outliers')
    sc2 = axes.scatter(ref[np.invert(outlier_index)], data[np.invert(outlier_index)], marker = 'o', color = 'b', s = 25, label = 'Readouts')
    sc1.set_facecolor("none")
    sc2.set_facecolor("none")
    axes.plot(thres_x, thres_y1, linestyle = '--', color = 'r', label = "R-Square = " + "{:.2f}".format(R_Square))
    axes.plot(thres_x, thres_y2, linestyle = '--', color = 'r', label = "y = " + "{:.2f}".format(fitting_coe[0]) + " x + " + "{:.2f}".format(fitting_coe[1]))
    axes.plot(np.array([0, boundary]), regression(np.array([0, boundary])), linestyle = "--", color = "k", alpha = 0.5)
    final_title_str = (title_str + "\nAccuracy % within " + str(bias) + " mg/dL = " + "{:.2f}".format(acc * 100)
                       + " %, Outliers: " + str(np.sum(outlier_index)) + "/" + str(ref.size))
    axes.set_title(final_title_str)
    axes.legend()
    if save_path != '':
        plt.savefig(save_path)
    plt.show()
    return 0
