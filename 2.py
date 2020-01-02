
import Producer
import time
import Process


def test(timeslice: int):

    Producer.readAndPrint()
    queue, loc = Producer.load("ciccio")
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
    print(waitingTimesMap)
    print("\n")

    for x in toRemove:
        waitingTimesMap.pop(x)


if __name__ == '__main__':
    test(2)