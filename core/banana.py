import cv2 as cv
import time

# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Load the model 
net = cv.dnn.readNet('models/face-person-detection-retail-0002.xml', 'models/face-person-detection-retail-0002.bin')
# Specify target device 
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)
# Read an image
print("Finish loading net")
frame = cv.imread('test3.jpg')
frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25, interpolation=cv.INTER_NEAREST)
cv.imwrite("1.jpg", frame)
# Prepare input blob and perform an inference 
blob = cv.dnn.blobFromImage(frame, size=(frame.shape[1],frame.shape[0]), ddepth=cv.CV_8U)
net.setInput(blob)
out = net.forward()
count = 0
t1 = time.time()
# Draw detected faces on the frame.
for detection in out.reshape(-1, 7):
    confidence = float(detection[2])
    xmin = int(detection[3] * frame.shape[1])
    ymin = int(detection[4] * frame.shape[0])
    xmax = int(detection[5] * frame.shape[1])
    ymax = int(detection[6] * frame.shape[0])
    if confidence > 0.5:
        cv.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))
        count += 1
        # Save the frame to an image file.
print(time.time() - t1)
cv.imwrite('out.png', frame)
#blob = cv.dnn.blobFromImage(frame, 1/255, size=(672, 384), ddepth=cv.CV_8U, crop=True) 
