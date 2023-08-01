def is_safe_state(available, max_claim, allocation):
    # Get the number of resources and processes
    num_resources = len(available)
    num_processes = len(max_claim)

    # Create a copy of available resources (work) and initialize finish array
    work = available.copy()
    finish = [False] * num_processes

    while True:
        found = False
        # Iterate through each process
        for i in range(num_processes):
            # Check if the process is not finished and if it can be executed
            if not finish[i] and all(work[j] >= max_claim[i][j] - allocation[i][j] for j in range(num_resources)):
                found = True
                # Mark the process as finished
                finish[i] = True
                # Add the allocated resources to the work vector
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                break

        # If no process can be executed, break out of the loop
        if not found:
            break

    # Check if all processes have finished (i.e., system is in a safe state)
    return all(finish)

def deadlock_detection(available, max_claim, allocation):
    # Check if the current state is safe or in a deadlock
    if is_safe_state(available, max_claim, allocation):
        print("The system is in a safe state. No deadlock detected.")
    else:
        print("Deadlock detected. The system is in an unsafe state.")

if __name__ == "__main__":
    # Define the available resources, maximum claim of each process, and current allocation
    available_resources = [3, 3, 2]
    max_claim_per_process = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    current_allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Perform deadlock detection
    deadlock_detection(available_resources, max_claim_per_process, current_allocation)

    # case 2
    # Define the deadlock scenario
    available_resources = [2, 2, 2]
    max_claim_per_process = [
        [3, 2, 2],
        [1, 2, 4],
        [4, 4, 3],
        [2, 3, 2]
    ]
    current_allocation = [
        [0, 1, 0],
        [0, 0, 1],
        [2, 1, 1],
        [1, 0, 0]
    ]

    # Perform deadlock detection
    deadlock_detection(available_resources, max_claim_per_process, current_allocation)
