from pypylon import pylon
import config.CaptureConfig as CaptureConfig
from acquisition.GlobalAcquisition import GlobalAcquisition

"""
https://docs.baslerweb.com/triggered-image-acquisition

"""
"""
Continuous triggered acquisition, where exposure start and stop are determined by
incoming rising and falling edges respectively
"""
class ContinuousTriggeredAcquisition(GlobalAcquisition):
    def __init__(self, captureConfig=CaptureConfig.CaptureConfig()):
        super.__init__()
        self.camera.AcquisitionMode.Value = "Continuous"

        #set the camera up to respond to signals from two lines.
        self.camera.ExposureMode.Value = "TriggerControlled"

        self.camera.LineSelector.Value = "Line1"
        self.camera.LineMode.Value = "Input"
        self.camera.TriggerSelector.Value = "ExposureActive"
        self.camera.TriggerMode.Value = "On"
        self.camera.TriggerActivation.Value = "LevelHigh"
        self.camera.TriggerSource.Value = "Line1"

        # for line in ["Line1", "Line2"]:
        #       self.camera.LineSelector.Value = line
        #       self.camera.LineMode.Value = "Input"

        #       self.camera.TriggerSelector.Value = "ExposureStart"
        #       self.camera.TriggerMode.Value = "On"
        #       self.camera.TriggerActivation.Value = "RisingEdge"
        #       self.camera.TriggerSource.Value = line

        #       self.camera.TriggerSelector.Value = "ExposureEnd"
        #       self.camera.TriggerMode.Value = "On"
        #       self.camera.TriggerActivation.Value = "FallingEdge"
        #       self.camera.TriggerSource.Value = line
              #todo it should actually be ExposureActive LevelHigh for these bad boys aye

        #set max framerate
        if captureConfig.maxFrameRate > 0:
            self.camera.AcquisitionFrameRateEnable = "true"
            self.camera.AcquisitionFrameRateAbs = captureConfig.maxFrameRate

    def start_acquistion(self):
        self.camera.AcquisitionStart.Execute()

    def stop_acquisition(self):
        self.camera.AcquisitionStop.Execute()
    
    def abort(self):
        self.camera.AcquisitionAbort.Execute()


