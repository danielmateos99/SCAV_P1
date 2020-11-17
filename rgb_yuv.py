import numpy as np

def rgb2yuv(rgb):
    m = np.array([
        [0.29900, -0.147108,  0.614777],
        [0.58700, -0.288804, -0.514799],
        [0.11400,  0.435912, -0.099978]
    ])
    yuv = np.dot(rgb, m)
    yuv += 0.5
    return yuv

def yuv2rgb(yuv):
    m = np.array([
        [1.000,  1.000, 1.000],
        [0.000, -0.394, 2.032],
        [1.140, -0.581, 0.000],
    ])
    yuv -= 0.5
    rgb = np.dot(yuv, m)
    return rgb


rgb_values = np.array([100,40,200])

print("Original RGB values:",rgb_values)
print("Estimated YUV values from the RGB ones:",rgb2yuv(rgb_values))
print("Estimated RGB values from the YUV ones:",yuv2rgb(rgb2yuv(rgb_values)))
