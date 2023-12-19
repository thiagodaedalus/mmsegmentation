from pathlib import Path

import cv2
import numpy as np


def main() -> None:
    dir = Path("/home/thiago/Downloads/project-3-at-2023-12-19-21-51-72712f76")
    a = np.load(dir / "task-1-annotation-2-by-2-tag-background-0.npy")
    cv2.imwrite("tmp.png", a)


if __name__ == "__main__":
    main()
