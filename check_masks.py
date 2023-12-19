from pathlib import Path

import cv2
import numpy as np


def main() -> None:
    dataset_dir = Path("/home/thiago/source/daedalus/luminar/datasets/with_masks")
    images_dir = dataset_dir / "images"
    masks_dir = dataset_dir / "masks"

    for img_path, mask_path in zip(
        sorted(images_dir.iterdir()), sorted(masks_dir.iterdir())
    ):
        mask = cv2.imread(str(mask_path))
        print(mask.shape)
        break

    pass


if __name__ == "__main__":
    main()
