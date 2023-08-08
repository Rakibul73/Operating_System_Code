import multiprocessing
import time

def process_function(process_id, arrival_time, burst_time):
    print(f"Process {process_id} started execution at time {time.time()}")
    time.sleep(burst_time)
    print(f"Process {process_id} completed execution at time {time.time()}")


def fcfs_scheduling(processes):
    # Sort the processes based on their arrival time (ascending order)
    # This ensures that processes with earlier arrival times are scheduled first.
    processes.sort(key=lambda p: p[1])

    # Initialize the starting time of the first process as its arrival time
    current_time = processes[0][1]

    # Initialize variables to keep track of total waiting time and turnaround time
    waiting_time_total = 0
    turnaround_time_total = 0

    # Print the table header for the process details
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")

    # Iterate through each process in the sorted order
    for process in processes:
        # Unpack the process details (process ID, arrival time, and burst time)
        pid, arrival_time, burst_time = process

        # Calculate the waiting time for the current process, ensuring it is non-negative
        waiting_time = max(0, current_time - arrival_time)

        # Calculate the turnaround time for the current process
        turnaround_time = waiting_time + burst_time

        # Update the total waiting time and turnaround time
        waiting_time_total += waiting_time
        turnaround_time_total += turnaround_time

        # Print the details for the current process
        print(f"{pid}\t\t{arrival_time}\t\t{burst_time}\t\t{waiting_time}\t\t{turnaround_time}")


        
        # Add the print statements for the process execution
        # print(f"Process {pid} started execution at time {current_time}")
        # Update the current time to the completion time of the current process
        current_time += burst_time
        # print(f"Process {pid} completed execution at time {current_time}")


    # Calculate the average waiting time and turnaround time for all processes
    n = len(processes)
    avg_waiting_time = waiting_time_total / n
    avg_turnaround_time = turnaround_time_total / n

    # Print the average waiting time and average turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if __name__ == "__main__":
    # Example usage with user input for the number of processes
    n = int(input("Enter the number of processes: "))
    processes = []

    # Prompt the user to enter arrival time and burst time for each process
    print("\nEnter Process Arrival Time and Burst Time")
    for i in range(n):
        arrival_time = float(input(f"P[{i+1}] Arrival Time: "))
        burst_time = float(input(f"P[{i+1}] Burst Time: "))
        processes.append((i+1, arrival_time, burst_time))
    
    
    jobs = []
    for process in processes:
        process_id, arrival_time, burst_time = process
        p = multiprocessing.Process(target=process_function, args=(process_id, arrival_time, burst_time))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    print("All processes completed execution.")

    # Call the FCFS scheduling function with the list of processes
    fcfs_scheduling(processes)



