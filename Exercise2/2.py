from Exercise2 import Producer
import time
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def test(timeslice: int):

    Producer.readAndPrint()
    queue, loc = Producer.load("commands")
    actProcess = queue.remove_min()[1]
    remainingTimeSlices = actProcess.timeSlices

    while True:
        time.sleep(2)
        if actProcess is None:
            print("No job running")
        else:
            print("Executing " + actProcess.name)
            remainingTimeSlices -= 1
        if not queue.is_empty() and remainingTimeSlices <= 0:
            actProcess = queue.remove_min()[1]
            remainingTimeSlices = actProcess.timeSlices
        elif remainingTimeSlices <= 0:
            actProcess= None
        queueupdate(loc, queue, timeslice)


def queueupdate(waitingTimesMap, queue, maxWaitingTime):

    toRemove = []

    for locator in waitingTimesMap:
        waitingTimesMap[locator]+=1
        if waitingTimesMap[locator] >= maxWaitingTime:
            if locator._value.priority >= -19:
                locator._value.priority -= 1
            try:
                queue.update(locator, locator._value.priority, locator._value)
                waitingTimesMap[locator] = 0
            except ValueError as error:
                toRemove.append(locator)
    for x in toRemove:
        waitingTimesMap.pop(x)

def test2():

    commandQueue, x = Producer.loadFromFile("commands")
    waitingTimesMap = {}
    scheduleQueue = AdaptableHeapPriorityQueue()
    actProcess = None
    remainingTimeSlices = 0

    while Producer.readNext(commandQueue, waitingTimesMap, scheduleQueue) or not scheduleQueue.is_empty() or remainingTimeSlices > 0:

        if not scheduleQueue.is_empty() and remainingTimeSlices <= 0:
            actProcess = scheduleQueue.remove_min()[1]
            remainingTimeSlices = actProcess.timeSlices

        elif scheduleQueue.is_empty() and actProcess is None:
            print("No job running")

        if remainingTimeSlices <= 0:
            actProcess = None
        else:
            print("Executing " + actProcess.name)
            remainingTimeSlices -= 1
        queueupdate(waitingTimesMap, scheduleQueue, x)

        time.sleep(2)

    print("No more commands")


if __name__ == '__main__':
   # test(2)
    test2()

