import time
from functools import wraps

# A list to store the results for later analysis (like saving to a CSV)
BENCHMARK_RESULTS = []

def time_it(func):
    """
    Decorator that measures the execution time of a function 
    and stores the result with the input size N.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Determine input size N (critical for complexity analysis)
        # We assume the first argument is the main data structure (e.g., list, tree root)
        N = 0
        if args and hasattr(args[0], '__len__'):
            N = len(args[0])
        elif 'data' in kwargs and hasattr(kwargs['data'], '__len__'):
            N = len(kwargs['data'])
        else:
            # For tree-like structures where len() doesn't work, 
            # you might need a custom size function or pass N as a kwarg.
            N = kwargs.get('N', 'Unknown')

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        # 2. Store the result in a clean dictionary format
        BENCHMARK_RESULTS.append({
            'algorithm': func.__name__,
            'input_size_N': N,
            'time_seconds': execution_time,
            'timestamp': time.time()
        })

        # Print for immediate local verification
        print(f"| {func.__name__} (N={N}): {execution_time:.6f}s")

        return result
    return wrapper

def save_results_to_csv(filename="benchmark_data.csv"):
    """Saves the collected benchmark results to a CSV file."""
    import pandas as pd
    df = pd.DataFrame(BENCHMARK_RESULTS)
    df.to_csv(filename, index=False)
    print(f"\n✅ Results saved to {filename}")