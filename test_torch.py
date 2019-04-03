import numpy as np
import torch
import timeit

def test_matmul():
    return torch.mm(A, B)

if __name__ == "__main__":
    A = torch.Tensor(np.random.random((4, 3)))
    B = torch.Tensor(np.random.random((3, 4)))

    time_elapsed = timeit.timeit(test_matmul, number=100000)
    mean_time = time_elapsed / 100000. * 1e3
    print("mean time: %f ms" % time_elapsed)