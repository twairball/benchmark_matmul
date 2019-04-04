import tensorflow as tf
import timeit

def test_matmul():
    return tf.matmul(A, B)

if __name__ == "__main__":
    tf.enable_eager_execution()
    A = tf.random_normal([1000,1000])
    B = tf.random_normal([1000,1000])
    repeats = 1000
    time_elapsed = timeit.timeit(test_matmul, number=repeats)
    mean_time = time_elapsed / float(repeats) * 1e3
    print("Tensorflow matmul for shapes %s @ %s" % (A.shape, B.shape))
    print("Total time: %f sec for %d runs" % (time_elapsed, repeats))
    print("mean time: %f ms" % time_elapsed)