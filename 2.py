
import Producer
import time
import Process

def test():
    Producer.readAndPrint()
    queue = Producer.load("ciccio")

    actProcess = queue.remove_min()[1]
    remainingTimeSlices = actProcess.getTimeSlices()

    while True:
        time.sleep(2)
        if actProcess== None:
            print("No job running")
        else:
            print("Executing " + actProcess.getName())
            remainingTimeSlices -= 1
        if not queue.is_empty() and remainingTimeSlices<=0:
            actProcess = queue.remove_min()[1]
            remainingTimeSlices = actProcess.getTimeSlices()
        elif remainingTimeSlices<=0:
            actProcess= None



if __name__ == '__main__':
    test()