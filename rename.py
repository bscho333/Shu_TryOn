import glob
import os
import json
import shutil


class MatchCloth:

    def classification(self):
        img_dir = os.listdir('./Model-Image_deid')
        for img_name in img_dir:
            if img_name.split('_')[-1] == '000.jpg':
                shutil.copy(f"./Model-Image_deid/{img_name}", f"./Model-Image-deid-front/{img_name}")

    def process(self):
        img_dir = os.listdir('./Model-Image-deid-front')
        with open("wearing_info_train.json") as f:
            wearing_infos = json.load(f)
        for fname in img_dir:
            for wearing_info in wearing_infos:
                if wearing_info["wearing"] == fname:
                    cloth_name = wearing_info["main_top"]
                    shutil.copy(f'./Item-Image/{cloth_name}_F.jpg', f'./cloth/{str(i).zfill(5)}.jpg')
                    shutil.copy(f'./Model-Image_deid/{fname}', f'./image/{str(i).zfill(5)}.jpg')



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


