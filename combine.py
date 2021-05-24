import cv2
import glob


def combine_movie():
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    files = sorted(glob.glob('media/*.mp4'))

    movie = cv2.VideoCapture(files[0])
    fps = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)

    output = cv2.VideoWriter('combine_output.mp4', int(fourcc), fps, (int(width), int(height)))

    frame = None

    for i in files:
        movie = cv2.VideoCapture(i)

        if movie.isOpened():
            ret, frame = movie.read()
        else:
            ret = False

        while ret:
            output.write(frame)
            ret, frame = movie.read()


if __name__ == '__main__':
    combine_movie()
