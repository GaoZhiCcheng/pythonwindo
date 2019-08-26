def xie():
    print('等待接收处理任务...')
    while True:
        data =  (yield )
        print('接收到的任务：',data)

def producer():
    c = xie()
    c.__next__()
    for i  in  range(3):
        print('发送一个任务...','任务%d' % i)
        c.send('任务%d' % i)
if  __name__  ==  '__main__':
    producer()