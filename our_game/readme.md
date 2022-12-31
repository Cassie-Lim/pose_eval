# 人机交互-脊椎姿势检测和交互复健程序
v0.1
## 功能定义
## 总体设计
## 模块设计
### 主线程
`main/py`

开启检测线程和游戏线程，并用队列通信
### 线程间通信
检测线程将会将检测到的上下左右数据存放在列表中，分别是[上，下，左，右]，而后列表被放入队列，供提醒线程和游戏线程使用。


### 检测线程
在`detect.py`中

封装了一个检测线程类。实例化时，接受一个队列作为参数，用于通信。队列中存放一个列表，列表中有4个数字，包含上下左右的数据。

接口定义
```python
def run(self):
    for i in range(5):
        # TODO: 根据检测到的姿势设置detectMotion，例如detectMotion = [0,1,2,3]
        self.mailbox.put(detectMotion)
        time.sleep(1)
```

### 提醒线程

### 游戏线程
在`game.py`中

封装了一个检测线程类。实例化时，接受一个队列作为参数，用于通信。队列中存放一个列表。队列空，超时则退出。

```python
def run(self):  
    while(1):
        try:
            userMotion = self.mailbox.get(timeout = 5)
            # TODO: 根据接收到的数据（上下左右）控制游戏
        except:
            print("no more data, exit")
            break
```




