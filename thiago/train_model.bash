#!/bin/bash

set -o errexit
set -o nounset
set -o xtrace
set -o pipefail

SCRIPT_DIR="$(dirname "$(realpath -s "$0")")"
REPOSITORY_ROOT="$(realpath "$SCRIPT_DIR"/..)"
TRAIN_SCRIPT="${REPOSITORY_ROOT}/train.py"

# customize this, if necessary
MODEL_NAME="${MODEL_NAME:-test_model}"
MODEL_SCRIPT="${REPOSITORY_ROOT}/models/${MODEL_NAME}.py"

python \
    "$TRAIN_SCRIPT" \
    "$MODEL_SCRIPT"
