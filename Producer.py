
f = open("ciccio", "r")

for line in f:
    tmp = line.split(" ")
    scheduler_process = tmp[0]
    scheduler_priority = tmp[1]
    scheduler_lenght = tmp[2]
    print(scheduler_process, scheduler_priority, scheduler_lenght)

