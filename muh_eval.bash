script="demo/image_demo.py"
input="/home/thiago/source/daedalus/luminar/datasets/with_masks/images/0a285f89-i_240_int_img.png"
output="result.jpg"
pth=$(cat work_dirs/test_model/last_checkpoint)

python \
    "$script" \
    "$input" \
    models/test_model.py \
    "$pth" \
    --device cuda:0 \
    --opacity 1
