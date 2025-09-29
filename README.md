
# Car Door Status Detection

This local web-page project is used to detect whether car doors and hood are opened or not\
Data car view is taken real-time from "https://euphonious-concha-ab5c5d.netlify.app/"




## Installation

This project is created and tested in devices as bellow

    1. Intel Core i7-9750H 
    2. Nvidia GTX-1650 Max - Q (preferable to have Nvidia GPU for faster training and Inference) 
    3. Ubuntu 22.04 LTS 
    4. Cuda Toolkit Version : 12.8 
    5. Nvidia Driver 570.172.08


## Python Library
All used python library are listed in "environment.yml". You can automatically install all library i use using Anaconda

To Install Anaconda, click this link : https://www.anaconda.com/download

You can install Nvidia Driver On Ubuntu via Additional Driver. Make sure you choose version with "appropriate" one \
To choose, proper Cuda Toolkit version, type "nvidia-smi" on your console. It will show your GPU properties and maximum cuda version you can install \
 You can install Cuda Toolkit in this link : https://developer.nvidia.com/cuda-toolkit-archive



    
## Debugging 
1. Most Common error are due to Xlib can't find target window name. Make sure you open the car view page in different window with Car Door Status Detection Web-page


## License

[MIT](https://choosealicense.com/licenses/mit/)

