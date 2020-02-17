# -*- coding: utf-8 -*-
"""
线程安全的单例模式
"""

import threading
import time


def synchronized(func):
    func.__lock__ = threading.Lock()
    
    def synced_func(*args, **kw):
        with func.__lock__:
            return func(*args, **kw)
    
    return synced_func
    
    
def Singleton(cls):
    instances = {}
    
    @synchronized
    def get_instance(*args, **kw):
        if cls not in instances:
            # time.sleep(0.5) 测试
            instances[cls] = cls(*args, **kw)
        return instances[cls]
        
    return get_instance
    
    
def worker():
    single_test = Test()
    print('id:', id(single_test), ' thread_name:', threading.currentThread().name)
    

@Singleton
class Test(object):
    a = 1


if __name__ == '__main__':
    print('main run')
    task_list = []
    for _ in range(30):
        t = threading.Thread(target=worker)
        task_list.append(t)
        
    for task in task_list:
        task.start()
        
    for task in task_list:
        task.join()