def is_available(process_id, allocated, max_resources, need, available):
    # Check if all the available resources are greater than or equal to the process needs
    return all(need[process_id][i] <= available[i] for i in range(len(available)))

def safe_sequence(processes, allocated, max_resources, need, available, safe=[]):
    # Check if a safe-sequence is found and display it, or recursively find more safe sequences
    if len(safe) == len(processes):
        # If a safe-sequence is found, display it
        print("Safe sequence:", "->".join("P" + str(p + 1) for p in safe))
    else:
        for i in range(len(processes)):
            if i not in safe and is_available(i, allocated, max_resources, need, available):
                # Mark the process and update available resources
                marked = safe + [i]
                new_available = [available[j] + allocated[i][j] for j in range(len(available))]

                # Recursively find safe sequences with the updated state
                safe_sequence(processes, allocated, max_resources, need, new_available, marked)

# Driver code
if __name__ == "__main__":
    # Define the processes, allocated resources, maximum resources, and available resources
    processes = [0, 1, 2, 3]
    allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1]]
    max_resources = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2]]
    resources = [10, 5, 7]

    # Calculate the need matrix and available resources
    need = [[max_resources[i][j] - allocated[i][j] for j in range(len(resources))] for i in range(len(processes))]
    available = [resources[j] - sum(allocated[i][j] for i in range(len(processes))) for j in range(len(resources))]

    # Find and print all safe sequences
    print("Safe sequences are:")
    safe_sequence(processes, allocated, max_resources, need, available)

    # Calculate the total number of possible safe sequences
    total_safe_sequences = 2 ** len(processes) - 1
    print("Total safe sequences:", total_safe_sequences)
