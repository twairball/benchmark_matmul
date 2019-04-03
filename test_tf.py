import tensorflow as tf
import timeit

def test_matmul():
    return tf.matmul(A, B)

if __name__ == "__main__":
    tf.enable_eager_execution()
    A = tf.random_normal([4,3])
    B = tf.random_normal([3,4])

    time_elapsed = timeit.timeit(test_matmul, number=100000)
    mean_time = time_elapsed / 100000. * 1e3
    print("mean time: %f ms" % time_elapsed)