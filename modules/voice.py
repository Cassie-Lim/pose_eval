import cv2
import pyttsx3
import threading
from collections import deque

class Reminder:
    engine = None
    rate = None

    def __init__(self):
        self.engine = pyttsx3.init()

    def remind(self, info):
        self.engine.say(info)
        self.engine.runAndWait()


# track how long user's pose has been out of range
ANGLE_THRESHOLD = 10
TIME_THRESHOLD = 5
INTERVAL = 5
fps = 0
lr_frame_cnt = 0
forward_frame_cnt = 0

# used in reminder thread
msg_q = deque(maxlen=10)
cond = threading.Condition()


def reminder_work():
    global cond, msg_q
    reminder = Reminder()
    while 1:
        cond.acquire()
        if len(msg_q) == 0:
            cond.wait()
        # 处理队列中msg
        msg = msg_q.popleft()
        reminder.remind(msg)
        cond.release()


def voice_init(input_fps):
    assert input_fps != 0
    global fps
    fps = input_fps
    print(len(msg_q))
    # 创建reminder线程
    thread_reminder = threading.Thread(target=reminder_work)
    thread_reminder.start()
    print("Create voice reminder")


def track_state(lr_angle, forward_angle, img):
    global lr_frame_cnt, forward_frame_cnt, fps, msg_q, cond
    if abs(lr_angle - 90) > ANGLE_THRESHOLD:
        lr_frame_cnt += 1
        if lr_frame_cnt >= TIME_THRESHOLD * fps and (lr_frame_cnt - TIME_THRESHOLD * fps) % (INTERVAL * fps) == 0:
            cond.acquire()
            if lr_angle > 90:
                msg_q.append("Hello, please tilt your head to the right side!")
            else:
                msg_q.append("Hello, please tilt your head to the left side!")
            # 唤醒reminder
            cond.notify()
            cond.release()
    else:
        lr_frame_cnt = 0
    if abs(forward_angle) > ANGLE_THRESHOLD:
        forward_frame_cnt += 1
        if forward_frame_cnt >= TIME_THRESHOLD * fps and (forward_frame_cnt - TIME_THRESHOLD * fps) % (INTERVAL * fps) == 0:
            cond.acquire()
            msg_q.append("Please don't lean your head forward!")
            cond.notify()
            cond.release()
    else:
        forward_frame_cnt = 0
    cv2.putText(img,
                "Duration for l&r: {:.2f}".format(lr_frame_cnt / fps),
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.putText(img,
                "Duration for forward: {:.2f}".format(forward_frame_cnt / fps),
                (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
