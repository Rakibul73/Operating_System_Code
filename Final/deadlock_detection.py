def input_data():
    global n, r, max_claim, allocation, avail

    n = int(input("Enter the number of processes: "))
    r = int(input("Enter the number of resources: "))

    print("Enter the Maximum Claim Matrix:")
    max_claim = []
    for i in range(n):
        row = list(map(int, input().split()))
        max_claim.append(row)

    print("Enter the Allocation Matrix:")
    allocation = []
    for i in range(n):
        row = list(map(int, input().split()))
        allocation.append(row)

    print("Enter the Available Resources:")
    avail = list(map(int, input().split()))


def show_data():
    global n, r, max_claim, allocation, avail

    print("Process\tAllocation\tMax\t\tAvailable")
    for i in range(n):
        print(f"P{i + 1}\t\t{allocation[i]}\t\t{max_claim[i]}\t\t{avail}")


def is_safe_state():
    global n, r, max_claim, allocation, avail

    work = avail.copy()
    finish = [False] * n

    while True:
        found = False
        for i in range(n):
            if not finish[i] and all(work[j] >= max_claim[i][j] - allocation[i][j] for j in range(r)):
                found = True
                finish[i] = True
                work = [work[j] + allocation[i][j] for j in range(r)]
                break

        if not found:
            break

    return all(finish)


def deadlock_detection():
    if is_safe_state():
        print("The system is in a safe state. No deadlock detected.")
    else:
        print("Deadlock detected. The system is in an unsafe state.")


if __name__ == "__main__":
    print("********** Deadlock Detection Algo ************")
    input_data()
    show_data()
    deadlock_detection()
