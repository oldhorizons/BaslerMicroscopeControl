# BaslerMicroscopeControl

## Setup
1. install [pylon suite](https://www.baslerweb.com/en/downloads/software/) in developer mode.
2. activate your venv using """env\Scripts\activate""" (if on windows)
2. install [pypylon](https://github.com/basler/pypylon) using """pip install pypylon""" (documentation [here](https://github.com/basler/pypylon-samples))
3. install [nidaqmx](https://github.com/ni/nidaqmx-python) using """pip install nidaqmx""" (documentation [here](https://nidaqmx-python.readthedocs.io/en/stable/))
4. install nidaqmx drivers using """python -m nidaqmx installdriver"""
5. Install other libraries: matplotlib, 