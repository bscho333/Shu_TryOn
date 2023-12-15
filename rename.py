import glob
import os
import json
import shutil

# AI Hub Dataset을 VTON-HD 형식으로 바꿔주기 위한 코드
# data_dir과 target_dir만 바꿔주면 작동
data_dir = "/DL/Dataset/AI_Hub"
target_dir = "/DL/Dataset/VT_Hub"
for mode in ["train", "test"]:
    print(mode)
    with open(os.path.join(data_dir,mode,"origin/winfo.json")) as f:
        wearing_infos = json.load(f)
    # model_dir = os.listdir(os.path.join(data_dir, mode, "origin/Model-Image"))
    # for model_name in model_dir:
    i=0
    for wearing_info in wearing_infos:
        if wearing_info["wearing"].split("_")[-1] == "000.jpg":
            model_name = wearing_info["wearing"]
            cloth_name = wearing_info["main_top"]
            shutil.copy(f'{data_dir}/{mode}/origin/Model-Image/{model_name}', f'{target_dir}/{mode}/image/{str(i).zfill(5)}_00.jpg')
            shutil.copy(f'{data_dir}/{mode}/origin/Item-Image/{cloth_name}_F.jpg', f'{target_dir}/{mode}/cloth/{str(i).zfill(5)}_00.jpg')
            i+=1


