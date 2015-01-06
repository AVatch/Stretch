import cv2
from datetime import datetime


def main():
    print "Hi"


def video_capture(f, display=False):
    cap = cv2.VideoCapture(f)

    frame_rate = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    frame_width = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

    print "FPS:\t", frame_rate, "\t[", frame_width, ",", frame_height, "]"

    # Define the codec
    fourcc = cv2.cv.CV_FOURCC(*'MP4V')
    out = cv2.VideoWriter('output.mp4v',
                          fourcc,
                          frame_rate,
                          (int(frame_width), int(frame_height)))

    tic = datetime.now()
    frames = []
    while(cap.isOpened()):
        if (datetime.now() - tic).total_seconds() > 10:
            break
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(gray)

            # Write file
            out.write(frame)

        if display:
            #   Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_capture('reference_orange.mp4')
