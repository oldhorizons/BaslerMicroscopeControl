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
        if self.captureConfig.maxFrames != None:
            self.camera.StartGrabbingMax(self.captureConfig.maxFrames)
        else:
            self.camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
        self.acquire()

    def acquire(self):
        if self.camera.GetGrabResultWaitObject().Wait(0):
            print("Grab results wait in the output queue.")

        # All triggered images are still waiting in the output queue
        # and are now retrieved.
        # The grabbing continues in the background, e.g. when using hardware trigger mode,
        # as long as the grab engine does not run out of buffers.
        buffersInQueue = 0
        while self.camera.RetrieveResult(0, pylon.TimeoutHandling_Return):
            buffersInQueue += 1

        print("Retrieved ", buffersInQueue, " grab results from output queue.")

        # Stop the grabbing.
        self.camera.StopGrabbing()
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