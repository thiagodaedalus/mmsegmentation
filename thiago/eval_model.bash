#!/bin/bash

set -o errexit
set -o nounset
set -o xtrace
set -o pipefail

SCRIPT_DIR="$(dirname "$(realpath -s "$0")")"
REPOSITORY_ROOT="$(realpath "$SCRIPT_DIR"/..)"
EVAL_SCRIPT="${REPOSITORY_ROOT}/demo/image_demo.py"

# customize this, if necessary
EVAL_IMAGE="/home/thiago/source/daedalus/luminar/datasets/with_masks/images/0a285f89-i_240_int_img.png"
MODEL_SCRIPT="${REPOSITORY_ROOT}/models/test_model.py"
MODEL_WEIGHTS="$(cat ${REPOSITORY_ROOT}/work_dirs/last_checkpoint)"

python \
    "$EVAL_SCRIPT" \
    "$EVAL_IMAGE" \
    "$MODEL_SCRIPT" \
    "$MODEL_WEIGHTS" \
    --device cuda:0 \
    --opacity 1
