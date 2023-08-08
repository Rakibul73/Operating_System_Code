def input_data():
    global n, r, max_resources, allocated_resources, available_resources

    print("********** Banker's Algorithm ************")
    n = int(input("Enter the number of Processes: "))
    r = int(input("Enter the number of resources instances: "))

    print("Enter the Max Matrix:")
    max_resources = []
    for i in range(n):
        max_resources.append(list(map(int, input().split())))

    print("Enter the Allocation Matrix:")
    allocated_resources = []
    for i in range(n):
        allocated_resources.append(list(map(int, input().split())))

    print("Enter the available Resources:")
    available_resources = list(map(int, input().split()))


def show_data():
    global n, r, max_resources, allocated_resources, available_resources

    print("\nProcess\tAllocation\tMax\tAvailable")
    for i in range(n):
        print(f"\nP{i+1}\t {allocated_resources[i]} \t{max_resources[i]}", end=" ")
        if i == 0:
            print("\t", *available_resources, end=" ")


def calculate_need():
    global n, r, max_resources, allocated_resources, need

    need = [[0] * r for _ in range(n)]

    for i in range(n):
        for j in range(r):
            need[i][j] = max_resources[i][j] - allocated_resources[i][j]


def is_available(process_id):
    global need, available_resources

    for j in range(r):
        if need[process_id][j] > available_resources[j]:
            return False

    return True


def banker_algorithm():
    global n, r, max_resources, allocated_resources, available_resources, need

    finish = [0] * n
    safe_sequence = []
    flag = True

    while flag:
        flag = False
        for i in range(n):
            if not finish[i] and is_available(i):
                for j in range(r):
                    available_resources[j] += allocated_resources[i][j]
                finish[i] = 1
                flag = True
                safe_sequence.append(i)

    if len(safe_sequence) == n:
        print("\nSafe sequence:", end=" ")
        for i in safe_sequence:
            print(f"P{i+1}", end="")
            if i != safe_sequence[-1]:
                print(" ->", end="")
        print("\n\nThe system is in a safe state.")
    else:
        print("\nProcess P", end="")
        for i in range(n):
            if not finish[i]:
                print(i + 1, end="")
                if i != n - 1:
                    print(" ->", end="")
        print(" is in deadlock.")
        print("\n\nThe system is in an unsafe state.")


if __name__ == "__main__":
    input_data()
    show_data()
    calculate_need()
    banker_algorithm()
