from VideoCapture import Device
import time
today = time.strftime("%Y-%m-%d.%H.%M.%S")
imageName = today+"-image.jpg"
path = "C:\path\\"+imageName
cam = Device()
cam.saveSnapshot(path)
