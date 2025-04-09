from pypylon import pylon
import matplotlib.pyplot as plt
import config.CaptureConfig as CaptureConfig

class GlobalAcquisition:
    def __init__(self, captureConfig=CaptureConfig.CaptureConfig()):
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.Open()
        self.camera.Gain.Value = captureConfig.gaindB
        self.captureConfig = captureConfig
    
    def start_acquistion(self):
        print("Using device ", self.camera.GetDeviceInfo().GetModelName())
        # self.camera.AcquisitionStart.Execute()

    def stop_acquisition(self):
        self.camera.AcquisitionStop.Execute()
    
    def abort(self):
        self.camera.AcquisitionAbort.Execute()

    # def start_acquistion(self):
    #     #NB IS THIS ROLLING???
    #     self.camera.StartGrabbingMax(self.captureConfig.captureLength)

    #     while self.camera.IsGrabbing():
    #         grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    #         if grabResult.GrabSucceeded():
    #             # Access the image data.
    #             print("SizeX: ", grabResult.Width)
    #             print("SizeY: ", grabResult.Height)
    #             img = grabResult.Array
    #             print("Gray value of first pixel: ", img[0, 0])
    #             # plt.imshow(img)
    #             # plt.show()
    #         grabResult.Release()
    #     self.camera.Close()