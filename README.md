# Pose_eval
A demo to evaluate neck posture using Lightweight OpenPose. For UCAS HCI course. 

> Original repository : [Daniil-Osokin/lightweight-human-pose-estimation.pytorch: Fast and accurate human pose estimation in PyTorch. Contains implementation of "Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose" paper. (github.com)](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch)
>
> Paper： [Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose](https://arxiv.org/pdf/1811.12004.pdf)

---

## 1. 环境配置

- 创建conda环境

```bash
conda create -n pose python=3.7
conda activate pose
```

- 安装pytorch库（可使用以下连接下载一个版本匹配的轮子，下载速度更快）
  https://download.pytorch.org/whl/torch_stable.html

- 安装其他依赖库：

  ```bash
  pip install -r requirements.txt
  ```

> Note：如果你未下载Visual Studio的Build Tools，可能在安装pycocotools时遇到一些困难（其没有现成的轮子，需要用源码编译），可参考如下链接安装：
>
> [(7条消息) error: Microsoft Visual C++ 14.0 is required问题解法_alicee_2012的博客-CSDN博客](https://blog.csdn.net/alicee_2012/article/details/122726986?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-122726986-blog-89399825.pc_relevant_aa2&spm=1001.2101.3001.4242.1&utm_relevant_index=2)
>
> [(7条消息) 错误：cl: 命令行 error D8021 :无效的数值参数“/Wno-cpp”_点亮～黑夜的博客-CSDN博客_cl: 命令行 error d8021 :无效的数值参数“/wno-cpp”](https://blog.csdn.net/weixin_41010198/article/details/94053130)

## 2. Demo使用

demo.py参数解释：

```bash
usage: demo.py [-h] [--checkpoint-path CHECKPOINT_PATH]                     

               [--height-size HEIGHT_SIZE] [--video VIDEO] [--remind REMIND]
               
               [--images IMAGES [IMAGES ...]] [--cpu] [--track TRACK]        
               [--smooth SMOOTH]    
               
optional arguments:
  -h, --help            show this help message and exit
                        network input layer height size
  --video VIDEO         path to video file or camera id
  --remind REMIND       whether to enable voice reminder
  --images IMAGES [IMAGES ...]
                        path to input image(s)
  --cpu                 run network inference on cpu
  --track TRACK         track pose id in video
  --smooth SMOOTH       smooth pose keypoints

```

重要参数的额外解释：

- --video：

    可以使用`video`参数指定所需输入的视频文件，或者摄像机的id（如果是电脑内置摄像头请把id设为1，如果是外接相机，可以参考[这篇文章](https://blog.csdn.net/babybin/article/details/122044565)获取设备id）。

    当然，你也可以直接运行`python demo.py`使用我们提供的默认测试[^1] 用例。

    > [^1]: 视频无版权问题，来源：https://www.pexels.com/video/a-woman-seated-by-a-wooden-table-having-a-meal-while-in-a-conversation-3256821/

- --cpu：

  我们默认cpu选项是enable的，如果你电脑上有英伟达显卡，可以使用`--cpu False`以获取更好的计算性能。

- --remind：
  实时语音提示，默认开启，后期和游戏结合时可将之关闭，同时可以获得更快的计算速度；

