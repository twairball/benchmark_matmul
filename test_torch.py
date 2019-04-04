import numpy as np
import torch
import timeit

def test_matmul():
    return torch.mm(A, B)

if __name__ == "__main__":
    A = torch.Tensor(np.random.random((1000, 1000)))
    B = torch.Tensor(np.random.random((1000, 1000)))
    repeats = 1000
    time_elapsed = timeit.timeit(test_matmul, number=repeats)
    mean_time = time_elapsed / float(repeats) * 1e3
    print("PyTorch matmul for shapes %s @ %s" % (A.shape, B.shape))
    print("Total time: %f sec for %d runs" % (time_elapsed, repeats))
    print("mean time: %f ms" % time_elapsed)
    