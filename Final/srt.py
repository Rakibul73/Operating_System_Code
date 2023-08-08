def schedulingProcess(process_data):
    start_time = []
    exit_time = []
    s_time = 0
    process_working_sequence = []
    process_data.sort(key=lambda x: x[1])
    
    while True:
        ready_queue = [] 
        normal_queue = [] 
        temp = []  
        
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                ready_queue.append(temp)
                temp = []
            elif process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                normal_queue.append(temp)
                temp = []
        
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
            start_time.append(s_time)
            s_time = s_time + 1
            exit_time.append(s_time)
            process_working_sequence.append(ready_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            
            if process_data[k][2] == 0:
                process_data[k][3] = 1
                process_data[k].append(s_time)
        
        if len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + 1
            exit_time.append(s_time)
            process_working_sequence.append(normal_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1 
            if process_data[k][2] == 0: 
                process_data[k][3] = 1 
                process_data[k].append(s_time)
    
    t_time = calculateTurnaroundTime(process_data)
    w_time = calculateWaitingTime(process_data)
    printData(process_data, t_time, w_time, process_working_sequence , start_time , exit_time)

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

def printData(process_data, average_turnaround_time, average_waiting_time, process_working_sequence , start_time , exit_time):
    process_data.sort(key=lambda x: x[0])
    print("Process_ID\tArrival_Time\tRem_Burst_Time\tCompleted\tOrig_Burst_Time\tExit_time\tTurnaround_Time\tWaiting_Time")
    
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            print(process_data[i][j], end="\t\t")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')
    print(f'Average Waiting Time: {average_waiting_time}')
    print(f'Sequence of Process: {process_working_sequence}')
    

no_of_processes = int(input("Enter number of processes: "))
process_data = []

print("\nEnter Process Arrival Time and Burst Time")
for i in range(no_of_processes):
    temporary = []
    arrival_time = float(input(f"P[{i+1}] Arrival Time: "))
    burst_time = float(input(f"P[{i+1}] Burst Time: "))
    temporary.extend([i+1, arrival_time, burst_time, 0, burst_time])
    process_data.append(temporary)

schedulingProcess(process_data)


'''
3
0
3
5
7
2
14

ANS:
|  P1 | P3 | P2 | P3 |
0     3    5    12   24


'''