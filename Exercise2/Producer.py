from Exercise2.Process import Process
from TdP_collections.queue.array_queue import ArrayQueue
from TdP_collections.queue.array_queue import Empty



def loadFromFile(fileName: str):
    """Load command from file into an ArrayQueue.
    The first line contain an integer which is the max number of time-slices a process has to wait
    before its priority is increased by one (decreased in our case)"""

    file = open(fileName, "r")
    queue = ArrayQueue()
    firstIteration = True

    for line in file:
        if firstIteration:
            x = int(line.rstrip("\n"))
            firstIteration = False
        else:
            queue.enqueue(line.rstrip("\n"))

    return queue, x


def readNext(queue: ArrayQueue, waitingTimesMap, scheduleQueue):
    """read next line from ArrayQueue, if is a new job we create a process object,
        add it to the priority queue and create a new entry in the waiting times map"""

    try:
        line = (str)(queue.dequeue())
    except Empty as exception:
        return False



    if not line.rstrip("\n") == "no new job this slice":
        tmp = line.rstrip("\n").split(" ")
        scheduler_process = tmp[2]
        scheduler_length = int(tmp[5])
        scheduler_priority = int(tmp[8])

        p = Process(scheduler_process, scheduler_priority, scheduler_length)
        waitingTimesMap[scheduleQueue.add(p.priority, p)] = 0

    return True
