def calculate_need(need, max_resources, allocated_resources):
    # Calculate the need matrix for each process
    for i in range(len(max_resources)):
        for j in range(len(max_resources[0])):
            # Need = Maximum resources required - Allocated resources
            need[i][j] = max_resources[i][j] - allocated_resources[i][j]

def is_safe_state(processes, available_resources, max_resources, allocated_resources):
    # Initialize the need matrix with zeros
    need = [[0 for _ in range(len(available_resources))] for _ in range(len(processes))]

    # Calculate the need matrix for each process
    calculate_need(need, max_resources, allocated_resources)

    # Create a copy of available resources to keep track of available resources during simulation
    work = available_resources[:]

    # Create a list to keep track of finished processes, initially set to 0 (not finished)
    finish = [0] * len(processes)

    # Create an empty list to store the safe sequence of processes
    safe_sequence = []

    # Loop until all processes are finished or deadlock is detected
    while True:
        found = False
        for p in range(len(processes)):
            # Check if the process is not finished and if its needs can be satisfied with available resources
            if not finish[p] and all(need[p][j] <= work[j] for j in range(len(available_resources))):
                # Update the available resources by adding the allocated resources of the process
                work = [work[j] + allocated_resources[p][j] for j in range(len(available_resources))]
                # Mark the process as finished
                finish[p] = 1
                # Add the process to the safe sequence
                safe_sequence.append(p)
                found = True

        # If no process can finish in the current iteration, exit the loop
        if not found:
            break

    # If all processes are finished, the system is in a safe state
    if all(finish):
        print("System is in safe state.")
        print("Safe sequence is:", safe_sequence)
        return True
    else:
        print("System is not in safe state.")
        return False

# Driver code
if __name__ == "__main__":
    processes = [0, 1, 2, 3, 4]
    available_resources = [3, 3, 2]

    max_resources = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    allocated_resources = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Check if the system is in a safe state using Banker's Algorithm
    is_safe_state(processes, available_resources, max_resources, allocated_resources)
