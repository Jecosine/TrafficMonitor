import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc("M","P","E","G")
out = cv2.VideoWriter("output.mp4",fourcc, 24, (640, 480))
_, frame = cap.read()
count = 0
render_list = []
while _:
    count += 1
    _, frame = cap.read()
    cv2.imshow("frame", frame)
    if count > 200:
        render_list.pop(0)
    render_list.append(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break
for i in render_list:
    out.write(i)
out.release()