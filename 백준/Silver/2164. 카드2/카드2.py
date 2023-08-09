from sys import stdin
import queue

icard_num = int(stdin.readline())
qcard = queue.Queue()
qcard_size = icard_num
for i in range(1, icard_num+1):
    qcard.put(i)
while 1:
    # if qcard.qsize() == 1: # Timeout
    if qcard_size == 1:
        break
    qcard.get()
    qcard.put(qcard.get())
    qcard_size -= 1
print(qcard.get())