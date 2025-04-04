#Camera Settings
gaindB = 36                                     # camera gain, dB
captureModes = ["rolling", "triggered"]         # capture modes
lightModes = ["blue", "violet", "alternating"]  # light modes
captureLength = 10                              # capture length in frames

"""
Config class that deals with image acquisition.
"""
class CaptureConfig:
    def __init__(self, gain=gaindB, captureMode=captureModes[0], 
                 lightMode=lightModes[0], captureLength=captureLength):
        self.captureMode = captureMode
        self.lightMode = lightMode
        self.gain = gain
        self.captureLength = captureLength