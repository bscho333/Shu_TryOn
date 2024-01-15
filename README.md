# Shu_TryOn
#### 3rd YAICON Project - 슈의 의상실 2023 ver.
We performed Virtual Try-On task with AI Hub dataset.
### Team Members
* Beomsik Cho (YAI 11th)  
* Yoonsu Park (YAI 11th)  
* Uhyeon Cho (YAI 12th)  
* Jaeun Lee (YAI 12th)  
* Sunghoon Jung (YAI 12th)

## Prerequisite
First, clone our repository to your workspace.
```shell
pip install git
git clone https://github.com/bscho333/Shu_TryOn
```
Our Demo is based on Vessl Workspace. `vessl_init.sh` will install vessl package and download our checkpoints.  
AI Hub dataset has been modified to VT_Hub similar to VITON-HD dataset for training.
```shell
cd Shu_TryOn/
sh vessl_init.sh
```
<details>
<summary>Checkpoints Directory Tree</summary>

```
checkpoints
 ┣ emasc
 ┃ ┣ checkpoint
 ┃ ┃ ┗ checkpoint-40000
 ┃ ┃ ┃ ┣ pytorch_model.bin
 ┃ ┃ ┃ ┣ pytorch_model_1.bin
 ┃ ┃ ┃ ┣ pytorch_model_2.bin
 ┃ ┃ ┃ ┣ random_states_0.pkl
 ┃ ┃ ┃ ┣ scaler.pt
 ┃ ┃ ┃ ┗ scheduler.bin
 ┃ ┣ imgs_step_10000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_20000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_30000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_40000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ emasc_10000.pth
 ┃ ┣ emasc_20000.pth
 ┃ ┣ emasc_30000.pth
 ┃ ┗ emasc_40000.pth
 ┣ inversion
 ┃ ┣ checkpoint
 ┃ ┃ ┗ checkpoint-30000
 ┃ ┃ ┃ ┣ optimizer.bin
 ┃ ┃ ┃ ┣ pytorch_model.bin
 ┃ ┃ ┃ ┣ pytorch_model_1.bin
 ┃ ┃ ┃ ┣ pytorch_model_2.bin
 ┃ ┃ ┃ ┣ random_states_0.pkl
 ┃ ┃ ┃ ┣ scaler.pt
 ┃ ┃ ┃ ┗ scheduler.bin
 ┃ ┣ imgs_step_10000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_15000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_20000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_25000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_30000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ imgs_step_5000_paired
 ┃ ┃ ┗ upper_body
 ┃ ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ inversion_adapter_10000.pth
 ┃ ┣ inversion_adapter_15000.pth
 ┃ ┣ inversion_adapter_20000.pth
 ┃ ┣ inversion_adapter_25000.pth
 ┃ ┣ inversion_adapter_30000.pth
 ┃ ┗ inversion_adapter_5000.pth
 ┗ tps
 ┃ ┗ 79epoch
 ┃ ┃ ┗ checkpoint_last.pth
```
</details>
<details>
<summary>VT_Hub Directory Tree</summary>

```
VT_Hub
 ┣ test
 ┃ ┣ cloth
 ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ image
 ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 04392_00.jpg
 ┃ ┣ image-parse-v3
 ┃ ┃ ┣ 00000_00.png
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 04392_00.png
 ┃ ┗ openpose_json
 ┃ ┃ ┣ 00000_00_keypoints.json
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 04392_00_keypoints.json
 ┣ train
 ┃ ┣ cloth
 ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 18015_00.jpg
 ┃ ┣ image
 ┃ ┃ ┣ 00000_00.jpg
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 18015_00.jpg
 ┃ ┣ image-parse-v3
 ┃ ┃ ┣ 00000_00.png
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 18015_00.png
 ┃ ┗ openpose_json
 ┃ ┃ ┣ 00000_00_keypoints.json
 ┃ ┃ ┣ ...
 ┃ ┃ ┗ 18015_00_keypoints.json
 ┣ VT_Hub.zip
 ┣ test_pairs.txt
 ┗ train_pairs.txt
```
</details>

Also, conda should be installed. If not, install miniconda3 with `Miniconda3-latest-Linux-x86_64.sh` downloaded from `vessl_init.sh`

## Inference
First, create the `shu-tryon` environment with `environment.yml`
```shell
conda env create -f environment.yml
conda activate shu-tryon
```
Next, prepare the cloth and model image.
<details>
<summary>Prerequiring files</summary>

We prepared 3 clothes and 1 model for demo.  
But if you want to use arbitrary image, there are 5 files required.
1. `~/Shu_TryOn/input/cloth`: cloth image. 
2. `~/Shu_TryOn/input/image`: model image.
3. `~/Shu_TryOn/input/cloth-mask`: masked image of cloth.
4. `~/Shu_TryOn/input/image-parse-v3`: human segmentation image of model.
5. `~/Shu_TryOn/input/openpose_json`: estimated pose map json file of model image.

>Since the `3`, `4`, `5` files can be acquired by `inference.py`, you only need cloth and model image. Recommened type is `.jpg`.
</details>

Put your cloth and model `.jpg` image in `~/Shu_TryOn/input/cloth` and `~/Shu_TryOn/input/image`.  

Then, edit the `./input/test/test_pairs.txt`. This file guides the pair of each cloth and model image. Each pair should be on the same line, and cloth and model image should be splited with ' ' (space). The cloth image should be on left, and model image should be on right. Following highlight is the example:
> Cloth iamge: `cloth5_00.jpg`, `abc.jpg`  
> Model image: `abc.jpg`, `image5_00.jpg`  
> If you want to match `cloth5_00.jpg` with `image5_00.jpg` and `abc.jpg` with `def.jpg`, 
> 
> The `test_pairs.txt` should be edited like this:
> ```text
> cloth5_00.jpg image5_00.jpg
> abc.jpg def.jpg
> ```

Finally, run the commend below:
```shell
python inference.py
```

## Results
<img width="1979" alt="스크린샷 2024-01-16 오전 12 17 55" src="https://github.com/bscho333/Shu_TryOn/assets/118449997/fdb6805f-9123-4e6b-a842-1e9f6faad24d">
<img width="2390" alt="스크린샷 2024-01-16 오전 12 16 15" src="https://github.com/bscho333/Shu_TryOn/assets/118449997/33d1cd8d-512d-4c6f-872b-44aad96c2a59">