from PIL import Image
import time
import cv2
import os
import U2Net.u2net_load as u2net_load
import U2Net.u2net_run as u2net_run

img_input = "/root/Shu_TryOn/input/test/image"
cloth_input = "/root/Shu_TryOn/input/test/cloth"
cloth_mask = "/root/Shu_TryOn/input/test/cloth-mask"

# 1. Resizing the original image
orig_height = 1024
orig_width = 768
orig_ratio = 768/1024
imgs = os.listdir(img_input)
for img_path in imgs:
    img = cv2.imread(os.path.join(img_input, img_path))
    height, width, _ = img.shape
    if height == orig_height and width == orig_width:
        continue
    ratio = width/height
    if ratio > orig_ratio:  # width is larger than original
        new_height = height
        new_width = int(height * orig_ratio)
    else:
        new_width = width
        new_height = int(width / orig_ratio)
    # crop the image
    x_start = int((width - new_width) / 2)
    y_start = int((height - new_height) / 2)
    crop_img = img[y_start:height-y_start, x_start:width-x_start, :]
    # resize the image
    img = cv2.resize(crop_img, (orig_width, orig_height))
    cv2.imwrite(os.path.join(img_input, img_path), img)

# 2. For preparing cloth-mask
u2net = u2net_load.model(model_name='u2netp')
u2net_run.infer(u2net, cloth_input, cloth_mask)

# 3. For preparing image-parse-v3
os.system('python simple_parse/simple_extractor.py --dataset "lip" --model-restore "/root/Shu_TryOn/simple_parse/exp-schp-201908261155-lip.pth" --input-dir "/root/Shu_TryOn/input/test/image" --output-dir /root/Shu_TryOn/input/test/image-parse-v3')

# 4. For preparing openpose_json
os.system('python predict_pose.py --img_dir "./input/test/image" --model_path "./openpose/models/pose/body_25" --pose_dir "./input/test/openpose_json"')

# 5. Inferencing LaDI-VTON
os.system('python ladi-vton/src/inference.py')

print("Done!")

