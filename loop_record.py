import cv2
import sys

# read sysetm args
# usage: loop_record.py [dev] [fps] [time(s)] [output]
def get_args():
    args = sys.argv[1:]
    if len(args) <> 4:
        print("usage : loop_record.py [dev] [fps] [time(s)] [output]")
        return False
    else:
        dev, fps, t, output = args
        try:
            dev = int(dev)
            fps = int(fps)
            time = fps * int(time)
        except Exception as e:
            print("Invalid arg occurs error {0}".format(e))
            return False
        else:
            return True
def record_video(dev, fps, time, output):
    cap = cv2.VideoCapture(dev)
    #5 -> width
    #6 -> height
    #7 -> fps
    _, frame = cap.read()
    fourcc = cv2.VideoWriter_fourcc("M","P","E","G")
    out = cv2.VideoWriter("output.mp4", fourcc, 24, (640, 480))
    count = 0
    frame_list = []
    while(_):
        _, frame = cap.read()
        count += 1
        cv2.show("frame", frame)
        if count > time:
            frame_list.pop(0)
        frame_list.append(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    for i in frame_list:
        out.write(i)
    out.release()
def mainprocess():
    _ = get_args()
    if not _:
        return
    record_video(dev, fps, time, output)

if __name__ == "__main__":
    mainprocess()
