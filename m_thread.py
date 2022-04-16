import threading
import time
from queue import Queue
from time import sleep

import _thread


class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, m_queue):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.m_queue = m_queue

    def run(self) -> None:
        print('Starting ', self.thread_name)
        print_time(self.thread_name, self.m_queue)
        print('Exit ', self.thread_name)


def print_time(thread_name, m_queue):
    # 判断 队列是否为空，如果为空，则设置退出标志位为1，如果不为空，则从队列取出一个数据
    while not ExitFlag:
        threadLock.acquire()
        if not m_queue.empty():
            task = m_queue.get()
            threadLock.release()
            print('%s -> get one task: %s, current time is: %s' % (thread_name, task, time.asctime(time.localtime(time.time()))))
        else:
            threadLock.release()
        sleep(2)


# 定义变量
task_list = ['qwert', 'uouop', 'vxcm', 'zxcvb', 'asdfg', ]
ExitFlag = 0
threadNameList = ['thread-1', 'thread-2', 'thread-3']
threadObjs = []
threadID = 1
workQueue = Queue(10)
threadLock = threading.Lock()

# 创建线程
for tName in threadNameList:
    thread_Obj = MyThread(threadID, tName, workQueue)
    thread_Obj.start()
    threadObjs.append(thread_Obj)
    threadID += 1

# 填充队列
for task in task_list:
    threadLock.acquire()
    workQueue.put(task)
    threadLock.release()
# 等待队列为空
while not workQueue.empty():
    print("current workQueue size is:%d\n" % workQueue.qsize())
    sleep(1)
else:
    print("current workQueue size is:%d\n" % workQueue.qsize())

# workQueue.join()
# 通知线程退出
ExitFlag = 1

# 回收join每一个线程
for thread_Obj in threadObjs:
    thread_Obj.join()

#
print('all threads exiting...')

