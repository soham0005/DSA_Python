import multiprocessing
import time

# Function to count vowels in a string (single-threaded)
def count_vowels(input_str, result=None):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in input_str:
        if char in vowels:
            vowel_count += 1
    if result is None:
        return vowel_count
    else:
        result.put(vowel_count)

# Function to parallelize vowel counting
def parallel_count_vowels(input_string, num_processes):
    
    manager = multiprocessing.Manager()
    result = manager.Queue()

    
    if len(input_string) < num_processes:
        num_processes = len(input_string)

    
    chars_per_process = len(input_string) // num_processes


    processes = []

    
    for i in range(num_processes):
        start = i * chars_per_process
        end = (i + 1) * chars_per_process if i < num_processes - 1 else None
        sub_string = input_string[start:end]

        process = multiprocessing.Process(target=count_vowels, args=(sub_string, result))
        processes.append(process)
        process.start()

   
    for process in processes:
        process.join()

   
    total_vowel_count = 0
    while not result.empty():
        total_vowel_count += result.get()

    return total_vowel_count

if __name__ == "__main__":
    input_string = input("Enter the string: ")
    num_processes = int(input("Enter the number of processes: "))

   
    start_time = time.time()
    total_vowel_count_parallel = parallel_count_vowels(input_string, num_processes)
    end_time = time.time()

    parallel_execution_time = end_time - start_time

    
    start_time = time.time()
    total_vowel_count_single = count_vowels(input_string)
    end_time = time.time()

    single_execution_time = end_time - start_time

    
    print("Total Vowel Count (Multiprocessing):", total_vowel_count_parallel)
    print("Execution Time (Multiprocessing):", parallel_execution_time, "seconds")
    print("Total Vowel Count (Single-Threaded):", total_vowel_count_single)
    print("Execution Time (Single-Threaded):", single_execution_time, "seconds")
