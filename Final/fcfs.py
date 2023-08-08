process_working_sequence = []
def fcfs_scheduling(processes):
    processes.sort(key=lambda p: p[1])

    current_time = 0

    waiting_time_total = 0
    turnaround_time_total = 0
    system_idle_time = 0
    timeline = []
    

    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")

    for process in processes:
        pid, arrival_time, burst_time = process
        process_working_sequence.append(pid)
        
        # Calculate system idle time
        if current_time < arrival_time:
            system_idle_time += arrival_time - current_time
            timeline.append(current_time)
            current_time = arrival_time
        timeline.append(current_time)
        
        waiting_time = max(0, current_time - arrival_time)
        turnaround_time = waiting_time + burst_time
        waiting_time_total += waiting_time
        turnaround_time_total += turnaround_time

        print(f"{pid}\t\t{arrival_time}\t\t{burst_time}\t\t{waiting_time}\t\t{turnaround_time}")

        # Add the print statements for the process execution
        # print(f"Process {pid} started execution at time {current_time}")
        
        # Update the current time to the completion time of the current process
        current_time += burst_time
        # print(f"Process {pid} completed execution at time {current_time}")
    
    timeline.append(current_time)
    avg_waiting_time = waiting_time_total / len(processes)
    avg_turnaround_time = turnaround_time_total / len(processes)

    # Print the average waiting time and average turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print("Syetem utilization:", (1 - (system_idle_time / current_time ) )* 100, "%")
    print("Sequence of Processes:", process_working_sequence)
    
    print()
    for process in process_working_sequence:
        print("|   " , process, "    " , end="")
    print("|")
    for i in timeline:
        print(i , end="        ")

n = int(input("Enter the number of processes: "))
processes = []

print("\nEnter Process Arrival Time and Burst Time")
for i in range(n):
    arrival_time = float(input(f"P[{i+1}] Arrival Time: "))
    burst_time = float(input(f"P[{i+1}] Burst Time: "))
    processes.append((i+1, arrival_time, burst_time))

fcfs_scheduling(processes)






'''
3
0
8
.4
4
1
1


'''