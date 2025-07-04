import glob
import os

import cv2
from tqdm import tqdm


def combine_movie():
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

    files = sorted(glob.glob("media/*.mp4"))

    movie = cv2.VideoCapture(files[0])
    fps = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)

    # 出力用ディレクトリ作成
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ファイルを出力
    output_path = os.path.join(output_dir, "combine_output.mp4")
    output = cv2.VideoWriter(output_path, int(fourcc), fps, (int(width), int(height)))

    for path in files:
        file_name = os.path.basename(path)
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            tqdm.write(f"⚠️ {file_name} をスキップします")
            continue

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        with tqdm(total=total_frames, desc=file_name, unit="frame", leave=True) as pbar:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                output.write(frame)
                pbar.update(1)

        cap.release()

    output.release()
    print("動画ファイルの結合が完了しました")


if __name__ == "__main__":
    combine_movie()
