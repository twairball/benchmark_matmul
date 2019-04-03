import TensorFlow
import Dispatch

func main() {
    let A  = Tensor<Float>(randomNormal:[4,3])
    let B  = Tensor<Float>(randomNormal:[3,4])

    var times:[Double] = []
    for _ in 0...10000 {
        let start = DispatchTime.now()
        let _ = matmul(A, B)
    
        let end = DispatchTime.now()
        let nanoseconds = Double(end.uptimeNanoseconds - start.uptimeNanoseconds)
        let milliseconds = nanoseconds / 1e6
        times.append(milliseconds)
    }
    let mean_time = times.reduce(0.0, +) / Double(times.count)
    print("mean time: \(mean_time) ms")
}

main()