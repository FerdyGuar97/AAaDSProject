
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
            print("Executing " + actProcess.name+"\n")
            remainingTimeSlices -= 1
        if not queue.is_empty() and remainingTimeSlices <= 0:
            actProcess = queue.remove_min()[1]
            remainingTimeSlices = actProcess.timeSlices
        elif remainingTimeSlices <= 0:
            actProcess= None
        queueupdate(loc, queue, timeslice)


def queueupdate(loc, queue, timeslice):
    for x in loc:
        loc[x]+=1
        if loc[x] >= timeslice:
            x._value.priority -= 1
            try:
                queue.update(x, x._value.priority, x._value)
                loc[x]=0
            except ValueError as error:
                print("something")

if __name__ == '__main__':
    test(2)