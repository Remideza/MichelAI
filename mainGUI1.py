# -*- coding: utf-8 -*-
'''
MichelAI, designed by Rémi pouchain for Bend the Future first album
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import random
import sys
import time
import wave
import threading
import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(493, 527)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 471, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gFILENAME = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gFILENAME.setText("")
        self.gFILENAME.setObjectName("gFILENAME")
        self.horizontalLayout.addWidget(self.gFILENAME)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gFPSWANTED = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.gFPSWANTED.setMaximumSize(QtCore.QSize(50, 16777215))
        self.gFPSWANTED.setMinimum(5)
        self.gFPSWANTED.setMaximum(1000)
        self.gFPSWANTED.setProperty("value", 30)
        self.gFPSWANTED.setObjectName("gFPSWANTED")
        self.gridLayout_2.addWidget(self.gFPSWANTED, 1, 1, 1, 1)
        self.gWIDTH = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gWIDTH.setMaximumSize(QtCore.QSize(30, 16777215))
        self.gWIDTH.setMaxLength(3750)
        self.gWIDTH.setObjectName("gWIDTH")
        self.gridLayout_2.addWidget(self.gWIDTH, 1, 3, 1, 1)
        self.gHEIGTH = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gHEIGTH.setMaximumSize(QtCore.QSize(30, 16777215))
        self.gHEIGTH.setMaxLength(3750)
        self.gHEIGTH.setObjectName("gHEIGTH")
        self.gridLayout_2.addWidget(self.gHEIGTH, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.gUSETHEME = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.gUSETHEME.setObjectName("gUSETHEME")
        self.gridLayout_2.addWidget(self.gUSETHEME, 1, 6, 1, 1)
        self.gQUALITY = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.gQUALITY.setObjectName("gQUALITY")
        self.gQUALITY.addItem("")
        self.gQUALITY.addItem("")
        self.gQUALITY.addItem("")
        self.gridLayout_2.addWidget(self.gQUALITY, 1, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 130, 2511, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.gINFOTEXT = QtWidgets.QLabel(Dialog)
        self.gINFOTEXT.setGeometry(QtCore.QRect(10, 490, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.gINFOTEXT.setFont(font)
        self.gINFOTEXT.setText("")
        self.gINFOTEXT.setObjectName("gINFOTEXT")
        self.gPREVIEW = QtWidgets.QLabel(Dialog)
        self.gPREVIEW.setGeometry(QtCore.QRect(253, 210, 231, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gPREVIEW.setFont(font)
        self.gPREVIEW.setFrameShape(QtWidgets.QFrame.Box)
        self.gPREVIEW.setObjectName("gPREVIEW")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 471, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gNBVIDS = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.gNBVIDS.setMinimum(1)
        self.gNBVIDS.setMaximum(100)
        self.gNBVIDS.setProperty("value", 1)
        self.gNBVIDS.setObjectName("gNBVIDS")
        self.gridLayout.addWidget(self.gNBVIDS, 0, 1, 1, 1)
        self.gSENSIBILITY = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.gSENSIBILITY.setMaximum(1.0)
        self.gSENSIBILITY.setSingleStep(0.01)
        self.gSENSIBILITY.setProperty("value", 0.7)
        self.gSENSIBILITY.setObjectName("gSENSIBILITY")
        self.gridLayout.addWidget(self.gSENSIBILITY, 0, 3, 1, 1)
        self.gREALFRAMES = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.gREALFRAMES.setMinimum(1)
        self.gREALFRAMES.setMaximum(200)
        self.gREALFRAMES.setProperty("value", 5)
        self.gREALFRAMES.setObjectName("gREALFRAMES")
        self.gridLayout.addWidget(self.gREALFRAMES, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.gRANDOMIZETHEME = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.gRANDOMIZETHEME.setObjectName("gRANDOMIZETHEME")
        self.gridLayout.addWidget(self.gRANDOMIZETHEME, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.gRANDOMIZETHEMES = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.gRANDOMIZETHEMES.setMaximum(1000)
        self.gRANDOMIZETHEMES.setProperty("value", 500)
        self.gRANDOMIZETHEMES.setObjectName("gRANDOMIZETHEMES")
        self.gridLayout.addWidget(self.gRANDOMIZETHEMES, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 4, 1, 1)
        self.gIMGBUFFERSIZE = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.gIMGBUFFERSIZE.setMinimum(10)
        self.gIMGBUFFERSIZE.setMaximum(10006)
        self.gIMGBUFFERSIZE.setProperty("value", 100)
        self.gIMGBUFFERSIZE.setObjectName("gIMGBUFFERSIZE")
        self.gridLayout.addWidget(self.gIMGBUFFERSIZE, 1, 5, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 241, 126))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)
        self.gFREQGROUP = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.gFREQGROUP.setMinimum(1)
        self.gFREQGROUP.setMaximum(10)
        self.gFREQGROUP.setProperty("value", 3)
        self.gFREQGROUP.setObjectName("gFREQGROUP")
        self.gridLayout_3.addWidget(self.gFREQGROUP, 0, 1, 1, 1)
        self.gFLOORFREQARR = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.gFLOORFREQARR.setMaximum(100)
        self.gFLOORFREQARR.setProperty("value", 3)
        self.gFLOORFREQARR.setObjectName("gFLOORFREQARR")
        self.gridLayout_3.addWidget(self.gFLOORFREQARR, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)
        self.gZMAX = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.gZMAX.setProperty("value", 2.0)
        self.gZMAX.setObjectName("gZMAX")
        self.gridLayout_3.addWidget(self.gZMAX, 2, 1, 1, 1)
        self.gYMAX = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.gYMAX.setProperty("value", 1.0)
        self.gYMAX.setObjectName("gYMAX")
        self.gridLayout_3.addWidget(self.gYMAX, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 4, 0, 1, 1)
        self.gFFTDECREASE = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.gFFTDECREASE.setProperty("value", 1)
        self.gFFTDECREASE.setObjectName("gFFTDECREASE")
        self.gridLayout_3.addWidget(self.gFFTDECREASE, 4, 1, 1, 1)
        self.gESTIMATE = QtWidgets.QLabel(Dialog)
        self.gESTIMATE.setGeometry(QtCore.QRect(20, 490, 391, 21))
        self.gESTIMATE.setObjectName("gESTIMATE")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 120, 261, 16))
        self.label_3.setObjectName("label_3")
        self.gProgress = QtWidgets.QProgressBar(Dialog)
        self.gProgress.setGeometry(QtCore.QRect(10, 450, 471, 23))
        self.gProgress.setProperty("value", 0)
        self.gProgress.setObjectName("gProgress")
        self.gStart = QtWidgets.QPushButton(Dialog)
        self.gStart.setGeometry(QtCore.QRect(410, 490, 75, 23))
        self.gStart.setObjectName("gStart")
        self.retranslateUi(Dialog)
        self.gStart.clicked.connect(self.mainlogic)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MichelAI"))
        self.label.setText(_translate("Dialog", "Music file name :"))
        self.label_2.setText(_translate("Dialog", "FPS :"))
        self.gHEIGTH.setText(_translate("Dialog", "1080"))
        self.label_5.setText(_translate("Dialog", "Height :"))
        self.label_4.setText(_translate("Dialog", "Width :"))
        self.gWIDTH.setText(_translate("Dialog", "1920"))
        self.gUSETHEME.setText(_translate("Dialog", "Use custom theme"))
        self.gQUALITY.setItemText(0, _translate("Dialog", "LD"))
        self.gQUALITY.setItemText(1, _translate("Dialog", "MD"))
        self.gQUALITY.setItemText(2, _translate("Dialog", "HD"))
        self.label_3.setText(_translate("Dialog", "Advanced parameters"))
        self.gStart.setText(_translate("Dialog", "Start"))
        self.gPREVIEW.setText(_translate("Dialog", ""))
        self.label_8.setText(_translate("Dialog", "Real frames :"))
        self.label_6.setText(_translate("Dialog", "Number of vids:"))
        self.label_7.setText(_translate("Dialog", "Sensibility :"))
        self.gRANDOMIZETHEME.setText(_translate("Dialog", "Randomize theme"))
        self.label_9.setText(_translate("Dialog", "Randomized themes:"))
        self.label_10.setText(_translate("Dialog", "Img buffer:"))
        self.label_13.setText(_translate("Dialog", "Z max :"))
        self.label_11.setText(_translate("Dialog", "Frequency group :"))
        self.label_12.setText(_translate("Dialog", "Floor freq array:"))
        self.label_14.setText(_translate("Dialog", "Y max :"))
        self.label_15.setText(_translate("Dialog", "FFT Decrease :"))
        self.gESTIMATE.setText(_translate("Dialog", "ESTIMATE"))

    def randomindexes(self, themetable, rando, randos):
        if (themetable == False):
            themetable = [616, 723, 115, 451, 604, 475, 51, 113, 415, 417, 445, 488, 489, 599, 611, 646, 966, 967, 971,
                          506, 530, 607, 101, 108, 111, 494, 502, 507, 592, 644, 657, 696, 815, 902, 107, 441, 509, 753,
                          816, 440, 448, 545, 632, 715, 744, 487, 500, 554, 724, 812, 907, 991, 992, 993, 102, 409, 455,
                          470, 531, 629, 701, 714, 749, 807, 852, 995, 112, 340, 405, 406, 421, 476, 490, 518, 525, 584,
                          594, 623, 673, 739, 472, 510, 684, 0, 1, 2, 7, 25, 27, 29, 35, 300, 301, 390, 393, 401, 402,
                          404, 413, 425, 429, 444, 447, 459, 464, 471, 508, 526, 527, 528, 583, 600, 605, 624, 633, 643,
                          655, 725, 737, 818, 821, 949, 950, 951, 970, 972, 973, 974, 975, 976, 979, 980, 984, 486, 517,
                          535, 557, 577, 826, 948, 365, 437, 439, 512, 552, 574, 576, 590, 635, 677, 712, 719, 720, 825,
                          840, 881, 910, 938, 947, 977, 978, 70, 73, 88, 516, 533, 551, 661, 674, 703, 854, 879, 936,
                          72, 90, 366, 418, 426, 438, 450, 461, 484, 503, 513, 515, 529, 532, 541, 563, 582, 596, 619,
                          625, 638, 640, 662, 726, 736, 849, 873, 900, 968, 969, 21, 24, 28, 33, 34, 37, 71, 148, 388,
                          392, 453, 454, 473, 562, 606, 668, 695, 716, 747, 776, 783, 787, 845, 850, 855, 878, 908, 942,
                          76, 78, 89, 419, 427, 442, 514, 613, 626, 639, 663, 688, 780, 784, 828, 839, 844, 872, 875,
                          889, 904, 917, 941, 75, 77, 281, 296, 385, 387, 400, 452, 544, 546, 567, 572, 579, 588, 612,
                          622, 667, 722, 940, 65, 74, 295, 297, 304, 386, 449, 534, 540, 547, 556, 559, 685, 728, 837,
                          901, 911, 994, 618, 659, 5, 9, 31, 36, 43, 47, 149, 150, 221, 228, 290, 291, 294, 302, 308,
                          319, 320, 321, 339, 349, 350, 352, 353, 359, 364, 368, 382, 389, 391, 403, 420, 443, 460, 492,
                          553, 558, 571, 587, 589, 593, 595, 597, 598, 608, 614, 620, 627, 658, 664, 699, 704, 713, 721,
                          748, 755, 877, 954, 955, 957, 958, 963, 987, 989, 990, 69, 360, 435, 483, 538, 550, 679, 687,
                          708, 863, 899, 903, 52, 53, 55, 56, 63, 64, 79, 87, 92, 97, 110, 122, 130, 303, 305, 306, 307,
                          399, 407, 412, 432, 467, 469, 477, 491, 521, 524, 537, 543, 591, 617, 621, 656, 686, 700, 705,
                          732, 759, 857, 862, 892, 895, 920, 91, 121, 505, 682, 710, 898, 82, 93, 118, 127, 145, 160,
                          333, 408, 457, 458, 463, 474, 478, 497, 504, 511, 519, 520, 523, 536, 539, 542, 548, 586, 602,
                          615, 628, 689, 718, 772, 778, 801, 833, 846, 861, 876, 883, 888, 893, 924, 934, 945, 960, 985,
                          986, 39, 40, 45, 46, 48, 57, 80, 94, 98, 106, 109, 117, 119, 129, 244, 270, 271, 283, 288,
                          289, 327, 328, 332, 347, 358, 397, 398, 411, 422, 423, 424, 428, 430, 436, 446, 456, 462, 465,
                          522, 601, 609, 610, 649, 653, 702, 706, 707, 709, 727, 729, 730, 733, 738, 740, 754, 761, 766,
                          769, 773, 777, 796, 802, 804, 835, 865, 909, 923, 933, 943, 944, 959, 962, 983, 996, 96, 103,
                          585, 603, 672, 683, 691, 694, 871, 884, 887, 891, 896, 961, 964, 61, 62, 84, 95, 136, 325,
                          395, 431, 434, 569, 570, 581, 631, 642, 645, 647, 666, 669, 690, 693, 711, 746, 794, 800, 810,
                          820, 832, 843, 858, 866, 874, 915, 919, 921, 927, 932, 953, 956, 14, 42, 54, 59, 83, 86, 105,
                          123, 248, 277, 279, 298, 299, 309, 317, 324, 334, 363, 367, 394, 410, 414, 416, 466, 468, 479,
                          493, 496, 498, 499, 561, 564, 568, 573, 578, 580, 630, 636, 641, 648, 650, 660, 675, 680, 692,
                          697, 717, 731, 743, 745, 750, 756, 767, 788, 789, 791, 792, 798, 799, 806, 809, 813, 819, 822,
                          842, 853, 859, 860, 868, 882, 886, 897, 905, 906, 918, 925, 926, 928, 930, 931, 937, 939, 946,
                          952, 965, 988, 997, 100, 652, 665, 678, 751, 823, 827, 831, 841, 847, 894, 914, 922, 929, 935,
                          998, 3, 4, 6, 8, 10, 11, 12, 13, 15, 22, 26, 30, 32, 38, 41, 44, 49, 50, 58, 60, 66, 67, 68,
                          81, 85, 99, 104, 114, 116, 120, 124, 125, 126, 128, 131, 132, 137, 138, 139, 140, 141, 142,
                          143, 144, 146, 147, 151, 156, 161, 169, 260, 269, 272, 273, 274, 275, 278, 282, 284, 285, 286,
                          287, 292, 293, 310, 311, 312, 313, 314, 315, 316, 318, 322, 323, 326, 329, 330, 331, 335, 338,
                          341, 348, 351, 354, 355, 356, 357, 361, 362, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378,
                          379, 380, 381, 383, 384, 396, 433, 480, 481, 482, 485, 495, 501, 549, 555, 560, 565, 566, 575,
                          634, 637, 651, 654, 670, 671, 676, 681, 698, 734, 735, 741, 742, 752, 757, 758, 760, 762, 763,
                          764, 765, 768, 770, 771, 774, 775, 779, 781, 782, 785, 786, 790, 793, 795, 803, 805, 808, 811,
                          814, 817, 824, 829, 830, 834, 836, 838, 848, 851, 856, 864, 867, 869, 870, 880, 885, 890, 912,
                          913, 981, 982, 999, 16, 17, 18, 19, 20, 133, 134, 135, 152, 23, 153, 276, 280, 336, 337, 154,
                          155, 157, 158, 159, 162, 163, 164, 165, 166, 167, 168, 170, 171, 172, 173, 174, 175, 176, 177,
                          178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196,
                          197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
                          216, 217, 218, 219, 220, 222, 223, 224, 225, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236,
                          237, 238, 239, 240, 241, 242, 243, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257,
                          258, 259, 261, 262, 263, 264, 265, 266, 267, 268, 342, 343, 344, 345, 346, 797, 916]
        if (not rando):
            return themetable
        else:
            t1 = themetable[:randos]
            random.shuffle(t1)
            return np.concatenate((t1, themetable[randos:]), axis=None)

    def getimage(self, noise, label, input_z, input_y, input_trunc, sess, output):
        return self.sample([noise], [label], input_z, input_y, input_trunc, sess, output)[0]

    def sample(self, noise, label, input_z, input_y, input_trunc, sess, output, truncation=1., batch_size=8):
        noise = np.asarray(noise)
        label = np.asarray(label)
        num = noise.shape[0]
        if len(label.shape) == 0:
            label = np.asarray([label] * num)
        if label.shape[0] != num:
            raise ValueError('Got # noise samples ({}) != # label samples ({})'.format(noise.shape[0], label.shape[0]))
        feed_dict = {input_z: noise, input_y: label, input_trunc: truncation}
        ims = sess.run(output, feed_dict=feed_dict)
        assert ims.shape[0] == num
        ims = np.clip(((ims + 1) / 2.0) * 256, 0, 255)
        ims = np.uint8(ims)
        return ims

    def threaded_mainlogic(self):
        t = threading.Thread(target=self.mainlogic())
        t.start()

    def mainlogic(self):
        self.gESTIMATE.setText("Loading ...")
        QtCore.QCoreApplication.processEvents()
        # SETTABLE PROPERTIES
        FILENAME = self.gFILENAME.text()
        FPSWANTED = int(self.gFPSWANTED.text())
        NBVIDS = int(self.gNBVIDS.text())
        SENSIBILITY = float(self.gSENSIBILITY.text().replace(',','.'))
        USETHEME = self.gUSETHEME.isChecked()
        RANDOMIZETHEME = self.gRANDOMIZETHEME.isChecked()
        RANDOMIZETHEMES = int(self.gRANDOMIZETHEMES.text())
        FREQGROUP = int(self.gFREQGROUP.text())
        IMGBUFFERSIZE = int(self.gIMGBUFFERSIZE.text())
        FLOORFREQARR = int(self.gFLOORFREQARR.text())
        WIDTH = int(self.gWIDTH.text())
        HEIGHT = int(self.gHEIGTH.text())
        ZMAX = float(self.gZMAX.text().replace(',','.'))
        YMAX = float(self.gYMAX.text().replace(',','.'))
        FFTDECREASE = int(self.gFFTDECREASE.text())
        REALFRAMES = int(self.gREALFRAMES.text())
        QUALITY = self.gQUALITY.currentText()

        # CALCULATED PROPERTIES
        INBETWEENFRAMES = int((FPSWANTED - REALFRAMES) / REALFRAMES)
        NOISESIZE = 128
        CATSIZE = 1000
        CEILFREQARR = FLOORFREQARR + 1000
        if (SENSIBILITY <= 0 or SENSIBILITY > 1):
            print()
            print("Sensibility must be > 0 and <= 1")
            sys.exit()
        INERTIA = 1 - SENSIBILITY

        if QUALITY == "HD":
            module_path = 'https://tfhub.dev/deepmind/biggan-deep-512/1'  # 512x512 BigGAN-deep
        elif QUALITY == "MD":
            module_path = 'https://tfhub.dev/deepmind/biggan-deep-256/1'  # 256x256 BigGAN-deep
        else:
            module_path = 'https://tfhub.dev/deepmind/biggan-deep-128/1'  # 128x128 BigGAN-deep

        inputs = dict([
            ('y', tf.placeholder(tf.float32, shape=[1, 1000])),
            ('z', tf.placeholder(tf.float32, shape=[1, 128])),
            ('truncation', tf.placeholder(tf.float32, shape=[]))
        ])

        module = hub.Module(module_path)
        output = module(inputs)

        input_y = inputs['y']
        input_z = inputs['z']
        input_trunc = inputs['truncation']

        initializer = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(initializer)

        path = os.getcwd()

        for iteration in range(0, NBVIDS):

            z = np.zeros(NOISESIZE)
            y = np.zeros(CATSIZE)
            maxFFTH = 0
            maxFFTL = 0
            allz = []
            ally = []
            wf = wave.open('input/' + FILENAME + '.wav', 'rb')
            frames = wf.getnframes()
            rate = wf.getframerate()
            CHUNK = int(rate / REALFRAMES)
            data = wf.readframes(CHUNK)
            first = True

            if not os.path.exists(path + '\\output\\' + FILENAME + '\\' + str(iteration)):
                os.makedirs(path + '\\output\\' + FILENAME + '\\' + str(iteration))

            if not USETHEME:
                randomctable = self.randomindexes(False, RANDOMIZETHEME, RANDOMIZETHEMES)
                file = open('output/' + FILENAME + '/' + str(iteration) + '/' + FILENAME + '.txt', "w")
                for i in randomctable:
                    file.write(str(i) + '\n')
                file.close()
            else:
                print("Using presaved theme")
                file = open('input/' + FILENAME + '.txt', "r+")
                randomctable = []
                for i in range(0, CATSIZE):
                    randomctable.append(int(file.readline()[:-1]))
                file.close()
                randomctable = self.randomindexes(randomctable, RANDOMIZETHEME, RANDOMIZETHEMES)

            while len(data) > 0:
                sdata = np.fromstring(data, dtype=np.int16)
                sdata = sdata * np.hamming(len(sdata))
                sfft = np.fft.fft(sdata)
                sfft = np.abs(sfft)
                bfft = sfft[:int(len(sfft) / 2)]
                # Nasty but effective way to do it
                while (len(bfft) % FREQGROUP != 0):
                    bfft = np.append(bfft, 0)
                fft = bfft.reshape(-1, FREQGROUP).mean(axis=1)
                if (len(fft) < CEILFREQARR):
                    print()
                    print("Sound spectrum to small, reduce REALFPS or FREQGROUP this might alter the generation")
                    print()
                    break

                # bass part
                bfft = fft[FLOORFREQARR:CEILFREQARR + NOISESIZE]
                fftlmax = np.max(bfft)
                if fftlmax > maxFFTL:
                    maxFFTL = np.max(np.abs(fftlmax))
                else:
                    maxFFTL = maxFFTL - (maxFFTL * (FFTDECREASE / 100))
                za = np.interp(bfft, (0, maxFFTL), (0, ZMAX))
                oz = np.array(z)
                for i in range(0, NOISESIZE):
                    z[i] = (INERTIA * z[i]) + (SENSIBILITY * za[i])

                # high part
                hfft = fft[FLOORFREQARR:CEILFREQARR]
                ffthmax = np.max(hfft)
                if ffthmax > maxFFTH:
                    maxFFTH = np.max(np.abs(ffthmax))
                else:
                    maxFFTH = maxFFTH - (maxFFTH * (FFTDECREASE / 100))
                ya = np.interp(hfft, (0, maxFFTH), (0, YMAX))
                oy = np.array(y)
                for i in range(0, CATSIZE):
                    y[randomctable[i]] = (INERTIA * y[randomctable[i]]) + (SENSIBILITY * ya[i])

                y = np.array(y)
                z = np.array(z)

                # Image
                if not first:
                    step = 1 / (INBETWEENFRAMES + 1)
                    for o in range(1, INBETWEENFRAMES + 1):
                        ally.append((oy * (1 - (step * o)) + y * (step * o)))
                        allz.append((oz * (1 - (step * o)) + z * (step * o)))
                else:
                    first = False

                ally.append(np.array(y))
                allz.append(np.array(z))

                data = wf.readframes(CHUNK)
            wf.close()
            video = cv2.VideoWriter('output/' + FILENAME + '/' + str(iteration) + '/video.mp4',
                                    cv2.VideoWriter_fourcc(*"mp4v"), (REALFRAMES + REALFRAMES * INBETWEENFRAMES),
                                    (WIDTH, HEIGHT))
            starttime = time.time()
            lastpc = 0
            realimages = []

            print('----------------------------------')
            print('             Starting')
            print('----------------------------------')

            for i in range(0, len(ally)):
                img = self.getimage(allz[i], ally[i], input_z, input_y, input_trunc, sess, output)
                color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                resize = cv2.resize(color, (WIDTH, HEIGHT))
                realimages.append(resize)

                completion = (i * 100) / len(ally)

                if len(realimages) > IMGBUFFERSIZE:
                    for imgs in realimages:
                        video.write(imgs)
                    realimages = []

                if int(completion) > lastpc:
                    cv2.imwrite('temp.jpg', cv2.resize(resize, (251,251)))
                    self.gPREVIEW.setPixmap(QtGui.QPixmap("temp.jpg"))
                    estimatesec = time.time() - starttime
                    starttime = time.time()
                    self.gProgress.setProperty("value", int(completion))
                    sys.stdout.write(
                        "Video " + str(iteration + 1) + "/" + str(NBVIDS) + " : " + str(
                            int(completion)) + "% remaining " + str(
                            (estimatesec * (100 - completion)) / 60)[:4] + " minuts \r")
                    self.gESTIMATE.setText("Video " + str(iteration + 1) + "/" + str(NBVIDS) + " : " + str(
                            int(completion)) + "% remaining " + str(
                            (estimatesec * (100 - completion)) / 60)[:4] + " minuts")
                    if int(completion) != 100:
                        sys.stdout.flush()
                    lastpc = int(completion)
                QtCore.QCoreApplication.processEvents()
            for imgs in realimages:
                video.write(imgs)
            cv2.destroyAllWindows()
            video.release()

            # combinaison de la video et de l'audio
            video = VideoFileClip('output/' + FILENAME + '/' + str(iteration) + '/video.mp4')
            video.write_videofile('output/' + FILENAME + '/' + str(iteration) + '/output.mp4',
                                  audio='input/' + FILENAME + '.mp3')
            self.gProgress.setProperty("value", 100)
        self.gESTIMATE.setText("DONE")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
