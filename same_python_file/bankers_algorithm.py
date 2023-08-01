class BankersAlgorithm:
    def __init__(self, max_resources, allocated_resources, total_resources):
        # Initialize the BankersAlgorithm class with the maximum resources required by each process,
        # currently allocated resources for each process, and total available resources in the system.
        self.max_resources = max_resources
        self.allocated_resources = allocated_resources
        self.total_resources = total_resources
        self.num_processes = len(max_resources)   # Number of processes in the system
        self.num_resources = len(total_resources) # Number of resource types in the system
        
        # Calculate the available resources by subtracting the currently allocated resources from the total resources
        self.available_resources = [total_resources[j] - sum(allocated_resources[i][j] for i in range(self.num_processes))
                                    for j in range(self.num_resources)]

    def is_safe_state(self, request, process_id):
        # Check if the requested resources exceed the maximum claim of the process
        if any(request[j] > self.max_resources[process_id][j] for j in range(self.num_resources)):
            return False

        # Check if the requested resources exceed the available resources
        if any(request[j] > self.available_resources[j] for j in range(self.num_resources)):
            return False

        # Temporarily allocate the requested resources to check for safety
        for j in range(self.num_resources):
            self.available_resources[j] -= request[j]
            self.allocated_resources[process_id][j] += request[j]

        # Perform safety check
        is_safe = self.check_safety()

        # Rollback the temporary allocation
        for j in range(self.num_resources):
            self.available_resources[j] += request[j]
            self.allocated_resources[process_id][j] -= request[j]

        return is_safe

    def check_safety(self):
        # Safety check to determine if the current system state is safe or not
        work = self.available_resources[:]  # Make a copy of available resources
        finish = [False] * self.num_processes  # Keep track of finished processes
        safe_sequence = []  # To store the sequence of processes that can finish without deadlock

        # Iterate until all processes are finished or deadlock is detected
        while True:
            found = False
            for i in range(self.num_processes):
                # Check if the current process can finish based on its needs and available resources
                if not finish[i] and all(self.max_resources[i][j] - self.allocated_resources[i][j] <= work[j]
                                         for j in range(self.num_resources)):
                    # If the process can finish, update the work and finish arrays
                    work = [work[j] + self.allocated_resources[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True
            # If no process can finish in the current iteration, exit the loop
            if not found:
                break
        
        # If all processes are finished, the system is in a safe state
        return all(finish)

# The main function to demonstrate the Banker's algorithm
if __name__ == "__main__":
    
    # case 1
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

    total_resources = [10, 5, 7]

    banker = BankersAlgorithm(max_resources, allocated_resources, total_resources)
    request = [1, 0, 2]
    process_id = 1

    if banker.is_safe_state(request, process_id):
        print("Request is safe to be granted.")
    else:
        print("Request may lead to a deadlock and cannot be granted.")


    # case 2
    max_resources = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
    ]

    allocated_resources = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
    ]

    total_resources = [10, 5, 7]

    banker = BankersAlgorithm(max_resources, allocated_resources, total_resources)
    request = [5, 0, 0]
    process_id = 0

    if banker.is_safe_state(request, process_id):
        print("Request is safe to be granted.")
    else:
        print("Request may lead to a deadlock and cannot be granted.")
