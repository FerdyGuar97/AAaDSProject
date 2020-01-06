from Exercise2 import Producer
import time
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def test(timeslice: int):
    # first we load command from file in a
    # auxiliary data structure
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
            actProcess = None
        queue_update(loc, queue, timeslice)


def queue_update(waiting_times_map, queue, maxWaitingTime):
    """Update of priority of processes in the priority queue due to time waited"""

    toRemove = []

    for locator in waiting_times_map:
        waiting_times_map[locator] += 1
        if waiting_times_map[locator] >= maxWaitingTime:
            if locator._value.priority >= -19:
                locator._value.priority -= 1
            try:
                queue.update(locator, locator._value.priority, locator._value)
                waiting_times_map[locator] = 0
            except ValueError as error:
                toRemove.append(locator)
    for x in toRemove:
        waiting_times_map.pop(x)


def test2():
    """
        test class with while loop

        end of test is:

        -no more command in array queue
        -no more process in priority queue
        -no running process

        each iteration check which process priorities to update

    """
    commandQueue, x = Producer.loadFromFile("commands")
    waitingTimesMap = {}
    scheduleQueue = AdaptableHeapPriorityQueue()
    actProcess = None
    remainingTimeSlices = 0

    while Producer.readNext(commandQueue, waitingTimesMap,
                            scheduleQueue) or not scheduleQueue.is_empty() or remainingTimeSlices > 0:

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
        queue_update(waitingTimesMap, scheduleQueue, x)

        time.sleep(2)

    print("No more commands")


if __name__ == '__main__':
    # test(2)
    test2()
