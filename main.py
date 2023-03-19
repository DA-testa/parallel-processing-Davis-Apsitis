# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    assigned_workers = [None] * m
    start_times = [None] * m
    next_free_time = [0] * n
    worker_heap = [(0, i) for i in range(n)]
    
    for i in range(m):
        duration = data[i]
        free_time, worker = heapq.heappop(worker_heap)
        output.append((worker, free_time))
        assigned_workers[i] = worker
        start_times[i] = free_time
        next_free_time[worker] = free_time + duration
        heapq.heappush(worker_heap, (next_free_time[worker], worker))
    return output

def main():
    # TODO: create input from keyboard
    #  
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
 
    n = 0
    m = 0

    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for worker, start_time in result:
      print(worker, start_time)

if __name__ == "__main__":
    main()

