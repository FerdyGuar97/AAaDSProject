
import Producer
import time as ciccio
from Process import Process

def test():
    Producer.readAndPrint()
    queue = Producer.load("ciccio")

    while not queue.is_empty():
        p=queue.remove_min()
        processPriority = p[0]
        processName = p[1].getName()
        processSlices = p[1].getTimeSlices()
        print(processName, processPriority, processSlices)
        ciccio.sleep(1)

if __name__ == '__main__':
    test()