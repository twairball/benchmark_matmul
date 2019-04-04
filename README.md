# Compare matmul speeds

Compares `matmul` speeds between `Swift for Tensorflow` vs `Numpy`. 

## Usage

````
# test swift
$ swift -O test_sw.swift 

# test python 
$ python test_np.py 
````

## Results

|  Lang  |  Platform  |  Ver   | Proc | mean (ms) | 
|--------|------------|--------|------|---------|
| Swift  | Tensorflow | v0.2   | CPU  |  8.4260 |
| Python | Numpy      | v1.151 | CPU  | 17.3245 |
| Python | PyTorch    | v0.4.1 | CPU  |  7.1645 | 
| Python | Tensorflow | v1.9.0 | CPU  |  7.2635 | 

##### Notes:
- Mac OSX / XCode 10
- python==v3.6.6
- swift==5.0-dev
- swift-tensorflow prebuilt from Mar-1, 2019 snapshot
- python-tensorflow run in eager-mode

## LICENSE

MIT 