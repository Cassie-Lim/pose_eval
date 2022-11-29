import math
import numpy as np
import cv2
import copy
import pyttsx3
import time

# track how long user's pose has been out of range
start = 0
end = 0


def calc_angle(p1, p2, cross):
    vec1 = np.array(p1 - cross)
    vec2 = np.array(p2 - cross)
    l1 = np.sqrt(vec1.dot(vec1))
    l2 = np.sqrt(vec2.dot(vec2))
    angle = np.arccos(vec1.dot(vec2) / (l1 * l2))
    angle = math.degrees(angle)
    return angle


def voice_remind(info):
    pp = pyttsx3.init()
    pp.say(info)
    pp.runAndWait()


def evaluate_pose(canvas, candidate, subset, front=True):
    global end
    global start
    if front:
        # 0:nose, 1:neck, 2: r_shoulder
        position = np.zeros((3, 2))
        # fetch confidence level
        confidence = subset[:, 18]
        # handle single person
        person = np.argmax(confidence)
        # without complete limbs
        target = subset[person][:3]
        if -1 in target:
            start = time.time()  # refresh cnt
            return canvas

        # locate critical point
        new_canvas = copy.deepcopy(canvas)
        for i in range(3):
            index = int(target[i])
            position[i] = candidate[index][0:2]
        # nose = candidate[0][0:2]
        # neck = candidate[1][0:2]
        # r_shoulder = candidate[2][0:2]
        # angle = calc_angle(nose, r_shoulder, neck)
        angle = calc_angle(position[0], position[2], position[1])
        end = time.time()
        cv2.putText(new_canvas,
                    "Neck & shoulder: {:.2f} degree".format(angle),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.putText(new_canvas,
                    "Duration: {:.2f}".format(end - start),
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        if abs(angle - 90) > 10:
            if end - start > 10:
                voice_remind("Hello, please watch your neck!")
        else:
            start = time.time()  # refresh cnt
    return new_canvas
