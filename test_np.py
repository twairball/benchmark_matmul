import numpy as np
import timeit

def test_matmul():
    return A @ B # matmul op

if __name__ == "__main__":
    A = np.random.random((1000, 1000))
    B = np.random.random((1000, 1000))
    repeats = 1000
    time_elapsed = timeit.timeit(test_matmul, number=repeats)
    mean_time = time_elapsed / float(repeats) * 1e3
    print("Numpy matmul for shapes %s @ %s" % (A.shape, B.shape))
    print("Total time: %f sec for %d runs" % (time_elapsed, repeats))
    print("mean time: %f ms" % time_elapsed)