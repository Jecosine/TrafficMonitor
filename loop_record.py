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

def mainprocess():
    _ = get_args()
    if not _:
        return
    record_video(dev, fps, time, output)


