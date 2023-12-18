crop_size = (300, 300)
data_preprocessor = dict(
    bgr_to_rgb=True,
    pad_val=0,
    seg_pad_val=255,
    size=(300, 300),
    type="SegDataPreProcessor",
)
data_root = "/home/thiago/source/daedalus/luminar/datasets/with_masks/"
dataset_type = "ExampleDataset"
default_hooks = dict(
    checkpoint=dict(by_epoch=False, interval=100, type="CheckpointHook"),
    logger=dict(interval=50, log_metric_by_epoch=False, type="LoggerHook"),
    param_scheduler=dict(type="ParamSchedulerHook"),
    sampler_seed=dict(type="DistSamplerSeedHook"),
    timer=dict(type="IterTimerHook"),
    visualization=dict(type="SegVisualizationHook"),
)
default_scope = "mmseg"
env_cfg = dict(
    cudnn_benchmark=True,
    dist_cfg=dict(backend="nccl"),
    mp_cfg=dict(mp_start_method="fork", opencv_num_threads=0),
)
img_ratios = [
    0.5,
    0.75,
    1.0,
    1.25,
    1.5,
    1.75,
]
load_from = None
log_level = "INFO"
log_processor = dict(by_epoch=False)
model = dict(
    auxiliary_head=[
        dict(
            align_corners=False,
            channels=32,
            concat_input=False,
            in_channels=128,
            in_index=-2,
            loss_decode=dict(
                loss_weight=0.4, type="CrossEntropyLoss", use_sigmoid=True
            ),
            norm_cfg=dict(momentum=0.01, requires_grad=True, type="SyncBN"),
            num_classes=19,
            num_convs=1,
            type="FCNHead",
        ),
        dict(
            align_corners=False,
            channels=32,
            concat_input=False,
            in_channels=64,
            in_index=-3,
            loss_decode=dict(
                loss_weight=0.4, type="CrossEntropyLoss", use_sigmoid=True
            ),
            norm_cfg=dict(momentum=0.01, requires_grad=True, type="SyncBN"),
            num_classes=19,
            num_convs=1,
            type="FCNHead",
        ),
    ],
    backbone=dict(
        align_corners=False,
        downsample_dw_channels=(
            32,
            48,
        ),
        fusion_out_channels=128,
        global_block_channels=(
            64,
            96,
            128,
        ),
        global_block_strides=(
            2,
            2,
            1,
        ),
        global_in_channels=64,
        global_out_channels=128,
        higher_in_channels=64,
        lower_in_channels=128,
        norm_cfg=dict(momentum=0.01, requires_grad=True, type="SyncBN"),
        out_indices=(
            0,
            1,
            2,
        ),
        type="FastSCNN",
    ),
    data_preprocessor=dict(
        bgr_to_rgb=True,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_val=0,
        seg_pad_val=255,
        size=(
            300,
            300,
        ),
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type="SegDataPreProcessor",
    ),
    decode_head=dict(
        align_corners=False,
        channels=128,
        concat_input=False,
        in_channels=128,
        in_index=-1,
        loss_decode=dict(loss_weight=1, type="CrossEntropyLoss", use_sigmoid=True),
        norm_cfg=dict(momentum=0.01, requires_grad=True, type="SyncBN"),
        num_classes=19,
        type="DepthwiseSeparableFCNHead",
    ),
    test_cfg=dict(mode="whole"),
    train_cfg=dict(),
    type="EncoderDecoder",
)
norm_cfg = dict(momentum=0.01, requires_grad=True, type="SyncBN")
optim_wrapper = dict(
    clip_grad=None,
    optimizer=dict(lr=0.12, momentum=0.9, type="SGD", weight_decay=4e-05),
    type="OptimWrapper",
)
optimizer = dict(lr=0.12, momentum=0.9, type="SGD", weight_decay=4e-05)
param_scheduler = [
    dict(begin=0, by_epoch=False, end=10000, eta_min=0.0001, power=0.9, type="PolyLR"),
]
resume = False
test_cfg = dict(type="TestLoop")
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_prefix=dict(img_path="images", seg_map_path="masks"),
        data_root="/home/thiago/source/daedalus/luminar/datasets/with_masks/",
        pipeline=[
            dict(type="LoadImageFromFile"),
            dict(
                keep_ratio=True,
                scale=(300, 300),
                type="Resize",
            ),
            dict(type="LoadAnnotations"),
            dict(type="PackSegInputs"),
        ],
        type="ExampleDataset",
    ),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=False, type="DefaultSampler"),
)
test_evaluator = dict(
    iou_metrics=[
        "mIoU",
    ],
    type="IoUMetric",
)
test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(
        keep_ratio=True,
        scale=(300, 300),
        type="Resize",
    ),
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]
train_cfg = dict(max_iters=10000, type="IterBasedTrainLoop", val_interval=10000)
train_dataloader = dict(
    batch_size=4,
    dataset=dict(
        data_prefix=dict(img_path="images", seg_map_path="masks"),
        data_root="/home/thiago/source/daedalus/luminar/datasets/with_masks/",
        pipeline=[
            dict(type="LoadImageFromFile"),
            dict(type="LoadAnnotations"),
            dict(
                keep_ratio=True,
                ratio_range=(
                    0.5,
                    2.0,
                ),
                scale=(300, 300),
                type="RandomResize",
            ),
            dict(
                cat_max_ratio=0.75,
                crop_size=(300, 300),
                type="RandomCrop",
            ),
            dict(prob=0.5, type="RandomFlip"),
            dict(type="PhotoMetricDistortion"),
            dict(type="PackSegInputs"),
        ],
        type="ExampleDataset",
    ),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=True, type="InfiniteSampler"),
)
train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(
        keep_ratio=True,
        ratio_range=(
            0.5,
            2.0,
        ),
        scale=(300, 300),
        type="RandomResize",
    ),
    dict(
        cat_max_ratio=0.75,
        crop_size=(
            300,
            300,
        ),
        type="RandomCrop",
    ),
    dict(prob=0.5, type="RandomFlip"),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
tta_model = dict(type="SegTTAModel")
tta_pipeline = [
    dict(backend_args=None, type="LoadImageFromFile"),
    dict(
        transforms=[
            [
                dict(keep_ratio=True, scale_factor=0.5, type="Resize"),
                dict(keep_ratio=True, scale_factor=0.75, type="Resize"),
                dict(keep_ratio=True, scale_factor=1.0, type="Resize"),
                dict(keep_ratio=True, scale_factor=1.25, type="Resize"),
                dict(keep_ratio=True, scale_factor=1.5, type="Resize"),
                dict(keep_ratio=True, scale_factor=1.75, type="Resize"),
            ],
            [
                dict(direction="horizontal", prob=0.0, type="RandomFlip"),
                dict(direction="horizontal", prob=1.0, type="RandomFlip"),
            ],
            [
                dict(type="LoadAnnotations"),
            ],
            [
                dict(type="PackSegInputs"),
            ],
        ],
        type="TestTimeAug",
    ),
]
val_cfg = dict(type="ValLoop")
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_prefix=dict(img_path="images", seg_map_path="masks"),
        data_root="/home/thiago/source/daedalus/luminar/datasets/with_masks/",
        pipeline=[
            dict(type="LoadImageFromFile"),
            dict(
                keep_ratio=True,
                scale=(300, 300),
                type="Resize",
            ),
            dict(type="LoadAnnotations"),
            dict(type="PackSegInputs"),
        ],
        type="ExampleDataset",
    ),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=False, type="DefaultSampler"),
)
val_evaluator = dict(
    iou_metrics=[
        "mIoU",
    ],
    type="IoUMetric",
)
vis_backends = [
    dict(type="LocalVisBackend"),
]
visualizer = dict(
    name="visualizer",
    type="SegLocalVisualizer",
    vis_backends=[
        dict(type="LocalVisBackend"),
    ],
)