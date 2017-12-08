## Multispectral Local Binary Pattern

python code for image processing

Adapted Local Binary Pattern for a Multispectral purpose (different spectra such as Visible and Infrared images)

### Install Dependecies

#### Python3

```
pip install numpy
```
### Calculate MSLBP
import on your code the MSLBP function & numpy package
```
from MSLBP import MSLBP
import numpy as np
```
input your two images to get the MSLBP image I and histogram h
```
[I,h]=MSLBP(I1,I2)
```

Paper reference : OMRI, Faten et FOUFOU, Sebti. A novel image texture fusion scheme for improving multispectral face recognition. In : Signal-Image Technology and Internet-Based Systems (SITIS), 2014 Tenth International Conference on. IEEE, 2014. p. 43-48.
