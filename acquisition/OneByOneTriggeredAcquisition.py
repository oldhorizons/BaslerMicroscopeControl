from pypylon import pylon
import config.CaptureConfig as CaptureConfig
from acquisition.GlobalAcquisition import GlobalAcquisition

class OneByOneTriggeredAcquisition(GlobalAcquisition):
    def __init__(self, captureConfig=CaptureConfig.CaptureConfig()):
        super.__init__(self, captureConfig)
        if captureConfig == None:
            self.camera.RegisterConfiguration(pylon.AcquireSingleFrameConfiguration())
        pylon.AcquireSingleFrameConfiguration.ApplyConfiguration()
        #set the camera up to respond to signals from two lines.
        self.camera.ExposureMode.Value = "TriggerControlled"

        self.camera.LineSelector.Value = "Line1"
        self.camera.LineMode.Value = "Input"
        self.camera.TriggerSelector.Value = "ExposureActive"
        self.camera.TriggerMode.Value = "On"
        self.camera.TriggerActivation.Value = "LevelHigh"
        self.camera.TriggerSource.Value = "Line1"





# for i in range(3):
#     if camera.WaitForFrameTriggerReady(200, pylon.TimeoutHandling_ThrowException):
#         camera.ExecuteSoftwareTrigger()