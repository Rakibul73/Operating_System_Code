
def schedulingProcess(process_data, time_slice):
    start_time = []
    exit_time = []
    process_working_sequence = []
    ready_queue = []
    s_time = 0
    process_data.sort(key=lambda x: x[1])

    while 1:
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][3] == 0:
                present = 0
                if len(ready_queue) != 0:
                    for k in range(len(ready_queue)):
                        if process_data[i][0] == ready_queue[k][0]:
                            present = 1

                if present == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []

                if len(ready_queue) != 0 and len(process_working_sequence) != 0:
                    for k in range(len(ready_queue)):
                        if ready_queue[k][0] == process_working_sequence[len(process_working_sequence) - 1]:
                            ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))

            elif process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        
        if len(ready_queue) != 0:
            if ready_queue[0][2] > time_slice:
                start_time.append(s_time)
                s_time = s_time + time_slice
                exit_time.append(s_time)
                process_working_sequence.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - time_slice
                ready_queue.pop(0)
            elif ready_queue[0][2] <= time_slice:
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                exit_time.append(s_time)
                process_working_sequence.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(s_time)
                ready_queue.pop(0)
        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            if normal_queue[0][2] > time_slice:
                start_time.append(s_time)
                s_time = s_time + time_slice
                exit_time.append(s_time)
                process_working_sequence.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - time_slice
            elif normal_queue[0][2] <= time_slice:
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                exit_time.append(s_time)
                process_working_sequence.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(s_time)
    t_time = calculateTurnaroundTime(process_data)
    w_time = calculateWaitingTime(process_data)
    printData(process_data, t_time, w_time, process_working_sequence)

def calculateTurnaroundTime(process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][5] - process_data[i][1]
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)
    return average_turnaround_time

def calculateWaitingTime(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][4]
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)
    return average_waiting_time

def printData(process_data, average_turnaround_time, average_waiting_time, process_working_sequence):
    process_data.sort(key=lambda x: x[0])
    print("Process_ID\tArrival_Time\tRem_Burst_Time\tCompleted\tOriginal_Burst_Time\tExit_Time\tTurnaround_Time\tWaiting_Time")
    
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):

            print(process_data[i][j], end="		")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')
    print(f'Average Waiting Time: {average_waiting_time}')
    print(f'Sequence of Processes: {process_working_sequence}')


no_of_processes = int(input("Enter number of processes: "))
process_data = []

print("\nEnter Process Arrival Time and Burst Time")
for i in range(no_of_processes):
    temporary = []
    arrival_time = float(input(f"P[{i+1}] Arrival Time: "))
    burst_time = float(input(f"P[{i+1}] Burst Time: "))
    temporary.extend([i+1, arrival_time, burst_time, 0, burst_time])
    process_data.append(temporary)

time_slice = int(input("Enter Time Slice: "))
schedulingProcess(process_data , time_slice)

'''

5
0
2
0
1
0
8
0
4
0
5



'''