import cv2

video = cv2.VideoCapture("test.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('trans.mp4', cv2.VideoWriter_fourcc(*'MP4V'), fps, size)  
success, frame = video.read()  
index = 1
while success :  
    cv2.putText(frame, 'fps: ' + str(fps), (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
    cv2.putText(frame, 'count: ' + str(frameCount), (0, 300), cv2.FONT_HERSHEY_SIMPLEX,2, (255,0,255), 5)
    cv2.putText(frame, 'frame: ' + str(index), (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
    cv2.putText(frame, 'time: ' + str(round(index / 24.0, 2)) + "s", (0,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.Laplacian(frame, cv2.CV_16S, ksize=3)
    frame = cv2.convertScaleAbs(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    
    cv2.imshow("new video", frame)
    cv2.waitKey(int(1000 / int(fps)))
    videoWriter.write(frame)
    success, frame = video.read()
    index += 1

video.release()
