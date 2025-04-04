from pypylon import pylon
import matplotlib.pyplot as plt
import config.CaptureConfig as CaptureConfig

class MainInterfacer:
    def __init__(self, captureConfig=CaptureConfig.CaptureConfig()):
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.Open()
        self.camera.Gain.Value = captureConfig.gaindB
        self.captureConfig = captureConfig

        # demonstrate some feature access
        # new_width = self.camera.Width.Value - self.camera.Width.Inc
        # if new_width >= self.camera.Width.Min:
        #     self.camera.Width.Value = new_width

    def start_acquistion(self):
        match self.captureConfig.captureMode:
            case "rolling":
                self.start_acquisition_rolling()
            case "triggered":
                self.start_acquisition_triggered()

    def start_acquisition_rolling(self):
        self.camera.StartGrabbingMax(self.captureConfig.captureLength)

        while self.camera.IsGrabbing():
            grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

            if grabResult.GrabSucceeded():
                # Access the image data.
                print("SizeX: ", grabResult.Width)
                print("SizeY: ", grabResult.Height)
                img = grabResult.Array
                print("Gray value of first pixel: ", img[0, 0])
                # plt.imshow(img)
                # plt.show()
            grabResult.Release()
        self.camera.Close()

    def start_acquisition_triggered(self):
        pass

if __name__ == "__main__":
    interfacer = MainInterfacer()
    interfacer.start_acquistion()