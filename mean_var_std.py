import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(numbers).reshape(3, 3)

    def collect(func):
        return [func(arr, axis=0).tolist(),
                func(arr, axis=1).tolist(),
                func(arr).item()]

    stats = {
        'mean': collect(np.mean),
        'variance': collect(np.var),
        'standard deviation': collect(np.std),
        'max': collect(np.max),
        'min': collect(np.min),
        'sum': collect(np.sum)
    }

    return stats
