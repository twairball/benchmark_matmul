# Compare matmul speeds

Compares `matmul` speeds between `Swift for Tensorflow` vs `Numpy`. 

## Requirements

`python v3.6.6`
`numpy==1.15.1`
`Swift 5.0-dev`
`Swift for Tensorflow v0.2 (March 1, 2019 snapshot)`

## Usage

````
# test swift
$ swift -O test_sw.swift 

# test python 
$ python test_np.py 
````

## Results

| Platform | mean (ms) | 
|----------|-----------|
| Swift Tensorflow | 0.010903 |
| Python Numpy | 0.088222 |

##### Notes:
- Mac OSX / XCode 10
- CPU only

## LICENSE

MIT 