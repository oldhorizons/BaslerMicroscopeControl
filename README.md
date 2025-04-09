# BaslerMicroscopeControl

## Setup
1. install [pylon suite](https://www.baslerweb.com/en/downloads/software/) in developer mode.
2. activate your venv using """env\Scripts\activate""" (if on windows)
2. install [pypylon](https://github.com/basler/pypylon) using """pip install pypylon""" (documentation [here](https://github.com/basler/pypylon-samples))
3. install [nidaqmx](https://github.com/ni/nidaqmx-python) using """pip install nidaqmx""" (documentation [here](https://nidaqmx-python.readthedocs.io/en/stable/))
4. install nidaqmx drivers using """python -m nidaqmx installdriver"""
5. Install other libraries: matplotlib

## Development Notes
Acquisition modes: [free run](https://docs.baslerweb.com/free-run-image-acquisition) vs [triggered](https://docs.baslerweb.com/triggered-image-acquisition)
Look into [built-in light control](https://docs.baslerweb.com/light-control)

### C++ Options
https://docs.baslerweb.com/pylonapi/cpp/sample_code#page-sample-code
https://docs.baslerweb.com/pylonapi/cpp/index_groups

### C# Options
[IStreamGrabber?!](https://docs.baslerweb.com/pylonapi/net/T_Basler_Pylon_IStreamGrabber#)

### Hardware
[Dedicated Frame Grabbers](https://www.baslerweb.com/en/acquisition-cards/frame-grabbers/#products)