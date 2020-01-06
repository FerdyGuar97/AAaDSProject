from Exercise2.Process import Process
from TdP_collections.queue.array_queue import ArrayQueue
from TdP_collections.queue.array_queue import Empty

def readAndPrint():
    """test method in which we open, read and print the contents of a text file"""

    file = open("commands", "r")
    for line in file:
        tmp = line.rstrip("\n").split(" ")
        scheduler_process = tmp[0]
        scheduler_priority = tmp[1]
        scheduler_length = tmp[2]
        scheduler_arrive = tmp[3]
       # print(scheduler_process, scheduler_priority, scheduler_length, scheduler_arrive)


def loadFromFile(fileName: str):
    """Load command from file into an ArrayQueue"""

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
