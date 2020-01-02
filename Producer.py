from Process import Process
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

def readAndPrint():
    file = open("ciccio", "r")

    for line in file:
        tmp = line.rstrip("\n").split(" ")
        scheduler_process = tmp[0]
        scheduler_priority = tmp[1]
        scheduler_length = tmp[2]
        scheduler_arrive = tmp[3]
       # print(scheduler_process, scheduler_priority, scheduler_length, scheduler_arrive)

def load(fileName: str):
    file = open(fileName, "r")
    queue = AdaptableHeapPriorityQueue()
    loc={}
    for line in file:
        tmp = line.rstrip("\n").split(" ")
        scheduler_process = tmp[0]
        scheduler_priority = int(tmp[1])
        scheduler_length = int(tmp[2])
        scheduler_arrive = int(tmp[3])
        p = Process(scheduler_process, scheduler_priority, scheduler_length)
        loc[queue.add(p.priority, p)] = 0
    return queue, loc