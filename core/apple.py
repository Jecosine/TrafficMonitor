import cv2 as cv
import time

# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def load_model():
    # Load the model 
    #net = cv.dnn.readNet('models/face-person-detection-retail-0002.xml', 'models/face-person-detection-retail-0002.bin')
    net = cv.dnn.readNet('models/face-detection-adas-0001.xml', 'models/face-detection-adas-0001.bin')
    # Specify target device 
    net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)
    # Read an image
    print("Finish loading net")
    return net
def process(net):
    count = 0
    cap = cv.VideoCapture("test.mp4")
    cap.set(3, 640)
    cap.set(4, 480)
    #cap = cv.VideoCapture(1)
    _, frame = cap.read()
    #fourcc = cv.VideoWriter_fourcc("M","P","E","G")
    #writer = cv.VideoWriter("output.mp4", fourcc, 24, (800, 480))
    while _:
        blob = cv.dnn.blobFromImage(frame, size=(640,480), ddepth=cv.CV_8U)
        net.setInput(blob)
        out = net.forward()
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
        print(count)
        cv.imshow("frame", frame)   
        if cv.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
        # Save the frame to an image file.
        #if count % 20 == 0:
        #    cv.imwrite("images/frame{0}.jpg".format(count), frame)
        #writer.write(frame)
        _, frame = cap.read()
    #writer.release()
    cap.release()
            
net = load_model()
process(net)

#frame = cv.imread('test3.jpg')
#frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25, interpolation=cv.INTER_NEAREST)
#cv.imwrite("1.jpg", frame)
## Prepare input blob and perform an inference 
#blob = cv.dnn.blobFromImage(frame, size=(frame.shape[1],frame.shape[0]), ddepth=cv.CV_8U)
#net.setInput(blob)
#out = net.forward()
#count = 0
#t1 = time.time()
#print(time.time() - t1)
#cv.imwrite('out.png', frame)
#blob = cv.dnn.blobFromImage(frame, 1/255, size=(672, 384), ddepth=cv.CV_8U, crop=True) 
