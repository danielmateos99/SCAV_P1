import numpy as np
from scipy.fftpack import fft, dct

input = np.array([4., 3., 5., 10.])
x =dct(input)
print(x)
