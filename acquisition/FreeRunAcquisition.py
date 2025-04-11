from pypylon import pylon
import config.CaptureConfig as CaptureConfig
from acquisition.GlobalAcquisition import GlobalAcquisition

class FreeRunAcquisition(GlobalAcquisition):
    def __init__(self, captureConfig=CaptureConfig.CaptureConfig()):
        super.__init__()
        self.camera.AcquisitionMode.Value = "Continuous"

        for line in ["Line1", "Line2"]:
            self.camera.LineSelector.Value = line
            self.camera.LineMode.Value = "Output"
            self.camera.LineSource.Value = "ExposureActive" #https://docs.baslerweb.com/line-source - consider FlashWindow?
            # also consider using a counter to swap values of two lines - https://docs.baslerweb.com/counter - could just use a microcontroller for that though it's NOT hard

        #clear triggers just in case previously set to a trigger
        for trigger in ["FrameStart", "FrameEnd", "FrameActive", 
                        "AcquisitionStart", "FrameBurstEnd", "FrameBurstActive", 
                        "ExposureStart", "ExposureEnd", "ExposureActive", "LineStart"]:
            self.camera.TriggerSelector.value = trigger
            self.camera.TriggerMode.Value = "Off"

        #set max framerate
        if captureConfig.maxFrameRate > 0:
            self.camera.AcquisitionFrameRateEnable = "true"
            self.camera.AcquisitionFrameRateAbs = captureConfig.maxFrameRate
