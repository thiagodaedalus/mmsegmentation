#!/bin/bash

set -o errexit
set -o nounset
set -o xtrace
set -o pipefail

SCRIPT_DIR="$(dirname "$(realpath -s "$0")")"
REPOSITORY_ROOT="$(realpath "$SCRIPT_DIR"/..)"
EVAL_SCRIPT="${REPOSITORY_ROOT}/demo/image_demo.py"

# customize this, if necessary
EVAL_IMAGE="/home/thiago/source/daedalus/luminar/datasets/road_segmentation/with_masks/subset-0123/images/742.png"
MODEL_NAME="${MODEL_NAME:-test_model}"
MODEL_SCRIPT="${REPOSITORY_ROOT}/models/${MODEL_NAME}.py"
MODEL_WEIGHTS="$(cat ${REPOSITORY_ROOT}/work_dirs/test_model/last_checkpoint)"

python \
    "$EVAL_SCRIPT" \
    "$EVAL_IMAGE" \
    "$MODEL_SCRIPT" \
    "$MODEL_WEIGHTS" \
    --device cuda:0 \
    --opacity 0.75
