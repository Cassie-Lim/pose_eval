import math
import time
import numpy as np


def calc_angle(p1, p2, cross):
    vec1 = np.array(p1 - cross)
    vec2 = np.array(p2 - cross)
    l1 = np.sqrt(vec1.dot(vec1))
    l2 = np.sqrt(vec2.dot(vec2))
    if l1 * l2 == 0:
        return 90
    angle = np.arccos(vec1.dot(vec2) / (l1 * l2))
    angle = math.degrees(angle)
    return angle


CALIBRATE_FRAME = 60
FOCAL_LEN = 2.8  # 相机焦距：2.8 mm
nn_cal_cnt = 0
sn_cal_cnt = 0
nose_neck_len = 0.0
rsho_neck_len = 0.0


def check_updown(nose, neck):
    global nn_cal_cnt, nose_neck_len
    vec = nose - neck
    nn_len = np.sqrt(vec.dot(vec))
    # 前十帧用于校准，初始化neck_len
    if nn_cal_cnt == 0:
        print("正在校准，请正对并平视镜头……( •̀ ω •́ )✧")
        time.sleep(2)
        nn_cal_cnt += 1
        return 0, 0
    elif nn_cal_cnt <= CALIBRATE_FRAME:
        nose_neck_len += nn_len
        nn_cal_cnt += 1
        if nn_cal_cnt == CALIBRATE_FRAME + 1:
            nose_neck_len /= CALIBRATE_FRAME
        return 0, 0
    up = 0
    down = 0
    # print(len / nose_neck_len)
    if nn_len / nose_neck_len > 1.5:
        up = 1
        # print("Up!")
    elif nn_len / nose_neck_len < 0.7:
        down = 1
        # print("Down!")
    return up, down


def distance_to_camera(true_len, f, display_len):
    # compute and return the distance from the maker to the camera
    return (true_len * f) / display_len


def check_anticollis(nose, neck, r_shoulder):
    global sn_cal_cnt, rsho_neck_len
    vec = neck - r_shoulder
    sn_len = np.sqrt(vec.dot(vec))
    # 前十帧用于校准，初始化shoulder_len
    if sn_cal_cnt == 0:
        sn_cal_cnt += 1
        return 0
    elif sn_cal_cnt <= CALIBRATE_FRAME:
        rsho_neck_len += sn_len
        sn_cal_cnt += 1
        if sn_cal_cnt == CALIBRATE_FRAME + 1:
            rsho_neck_len /= CALIBRATE_FRAME
        return 0
    ratio = sn_len / rsho_neck_len
    vec2 = nose - neck
    nn_len = np.sqrt(vec2.dot(vec2))
    cos_val = nn_len / ratio / nose_neck_len
    # print("Ratio:{} cos_val:{}".format(ratio, cos_val))
    if cos_val > 1:
        return 0
    return math.degrees(math.acos(cos_val))
