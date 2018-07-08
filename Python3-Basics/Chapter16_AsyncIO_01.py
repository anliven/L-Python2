# coding=utf-8
import threading
import time


def get_body(i):
    print("start", i)
    time.sleep(2)
    print("end", i)


for i in range(5):
    t = threading.Thread(target=get_body, args=(i,))
    t.start()

# ### 进程与线程
# 进程是应用程序的启动实例，拥有代码和打开的文件资源、数据资源、独立的内存空间，是资源分配的最小单位；
# 线程从属于进程，作为单一顺序的控制流被包含在进程之中，是进程中的实际运作单位，线程拥有自己的栈空间；
# 线程拥有自己的栈空间，是操作系统能够进行CPU运算调度的最小单位；
# 一个进程至少包含一个主线程，也可以并发多个线程，每个线程并行执行不同的任务；
# 简而言之，对操作系统来说，线程是最小的执行单元，进程是最小的资源管理单元；
# 相比进程，线程易于调度、开销少、利于提高并发性；
#
# ### 多线程的执行
# 在Python虚拟机按照以下方式执行：
# 1. 设置GIL；
# 2. 切换到一个线程去运行；
# 3. 运行指定数量的字节码指令，或者线程主动让出控制（调用time.sleep(0)）；
# 4. 把线程设置为睡眠状态；
# 5. 解锁GIL；
# 6. 再次重复以上所有步骤；
#
# ### GIL（Global Interpreter Lock，全局解释器锁）
# 由于GIL的限制，在解释器主循环（Python虚拟机）中，任意时刻，只能有一个线程在解释器中运行；
# GIL不是Python的特性，而是在实现Python解析器CPython时所引入的一个概念，在JPython中就没有GIL的概念；
# 也就是说，CPython的多线程并没有实现真正意义上的并发；
#
# ### 任务类型
# 在Python中，并发（concurrency）实现方式有三种：通过线程（threading）、多进程（multiprocessing）和Asyncio；
# 不同的方式适用不同的任务类型和场景；
# CPU（计算）密集型任务：由于GIL的存在，通常使用多进程来实现；
# IO密集型任务：
# - 通过线程调度来让线程在执行IO任务时让出GIL，从而实现表面上的并发；
# - 通过协程（运行在单线程当中的“并发”）；
#
# ### 协程（Coroutines）
# 协程是一种比线程更加轻量级的存在，一个线程可以拥有多个协程；
# 协程完全是由程序所控制（在用户态执行），而不是被操作系统内核所管理，性能得到很大提升，不会像线程切换那样消耗资源。