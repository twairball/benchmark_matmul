import TensorFlow
import Dispatch

func main() {
    let A  = Tensor<Float>(randomNormal:[1000,1000])
    let B  = Tensor<Float>(randomNormal:[1000,1000])

    var times:[Double] = []
    for _ in 0...10000 {
        let start = DispatchTime.now()
        let _ = matmul(A, B)
    
        let end = DispatchTime.now()
        let nanoseconds = Double(end.uptimeNanoseconds - start.uptimeNanoseconds)
        let milliseconds = nanoseconds / 1e6
        times.append(milliseconds)
    }
    let total_time_ms = times.reduce(0.0, +)
    let total_time_sec = total_time_ms / 1e3
    let mean_time = total_time_ms / Double(times.count)
    print("Swift-TF matmul for shapes \(A.shape) @ \(B.shape)")
    print("Total time: \(total_time_sec) sec for \(times.count) runs")
    print("mean time: \(mean_time) ms")
    }

main()