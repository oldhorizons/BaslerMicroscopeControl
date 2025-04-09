#Camera Settings
gaindB = 36                                     # camera gain, dB
captureModes = ["rolling", "triggered"]         # capture modes
lightModes = ["blue", "violet", "alternating"]  # light modes
captureLength = 10                              # capture length in frames
maxFrameRate = 0                                # maximum frame rate. <= 0 means no limit. NB acA1440-22uc has a default framerate of 227fps
maxFrames = None

"""
Config class that deals with image acquisition.
"""
class CaptureConfig:
    def __init__(self, gain=gaindB, captureMode=captureModes[0], lightMode=lightModes[0], captureLength=captureLength, maxFrameRate=maxFrameRate,
                 maxFrames=maxFrames):
        self.captureMode = captureMode
        self.lightMode = lightMode
        self.gain = gain
        self.captureLength = captureLength
        self.maxFrameRate = maxFrameRate
        self.maxFrames = maxFrames