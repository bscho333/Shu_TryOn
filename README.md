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
Next, put your cloth and model image in `~/Shu_TryOn/input/`

```shell
python simple_extractor.py --dataset "lip" --model-restore "C:\DL\Dataset\VT_Hub\backups\exp-schp-201908261155-lip.pth" --input-dir "C:\DL\Dataset\VT_Hub\test\image" --output-dir C:\DL\Dataset\VT_Hub\test\image-parse-v3
```

```shell
openpose.bin --image_dir /root/input/test/image --hand --disable_blending --display 0 --write_json {save_path} --num_gpu 1 --num_gpu_start 0
```