# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class ExampleDataset(BaseSegDataset):
    METAINFO = dict(
        classes=(["road", "roadside"]),
        palette=[[187, 158, 255], [255, 163, 158]],
    )

    def __init__(self, img_suffix=".png", seg_map_suffix=".png", **kwargs) -> None:
        super().__init__(img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
