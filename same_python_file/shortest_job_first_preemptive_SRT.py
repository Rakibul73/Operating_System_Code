class SJF:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            arrival_time = float(input(f"Enter Arrival Time for Process {process_id}: "))

            burst_time = float(input(f"Enter Burst Time for Process {process_id}: "))

            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)
        SJF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
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
                '''
                Sort processes according to Burst Time
                '''
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)
        SJF.printData(self, process_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("Process_ID  Arrival_Time  Rem_Burst_Time      Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
        
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="\t\t")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Process: {sequence_of_process}')


if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    sjf = SJF()
    sjf.processData(no_of_processes)


'''
3
1
0
8
2
.4
4
3
1
1


'''