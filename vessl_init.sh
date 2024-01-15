# Based on Vessl Workspace

# Project root
PROJECT_ROOT="/root/virtual"

#################################################################################
pip install vessl gdown

# miniforge download
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#sh Miniconda3-latest-Linux-x86_64.sh

# Cloth masking model checkpoints
gdown 1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy -O ${PROJECT_ROOT}/Shu_TryOn/U2Net/saved_models/u2netp/u2netp.pth
gdown 1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ -O ${PROJECT_ROOT}/Shu_TryOn/U2Net/saved_models/u2net/u2net.pth

# Human parsing checkpoint
gdown 1k4dllHpu0bdx38J7H28rVVLpU-kOHmnH -O ${PROJECT_ROOT}/Shu_TryOn/simple_parse/exp-schp-201908261155-lip.pth

# Openpose checkpoint
wget https://www.dropbox.com/s/3x0xambj2rkyrap/pose_iter_584000.caffemodel -P ${PROJECT_ROOT}/Shu_TryOn/openpose/models/pose/body_25

# Our dataset & checkpoints
vessl dataset download tps / ${PROJECT_ROOT}/checkpoints/tps/79epoch
vessl dataset download CLIP-Embedding / ${PROJECT_ROOT}/Shu_TryOn/ladi-vton/data
vessl dataset download inversion / ${PROJECT_ROOT}/checkpoints/
vessl dataset download emasc / ${PROJECT_ROOT}/checkpoints/
vessl dataset download VT-Hub / ${PROJECT_ROOT}/VT_Hub
cd VT_Hub || (echo VT-Hub did not downloaded && return)
unzip VT_Hub.zip
cd ..

    # # For libGL.so.1 error
    # su -
    # apt-get update
    # apt-get install sudo -y
    # sudo apt-get update
    # apt-get -y install libgl1-mesa-glx
    # # exit ---> Should be manually typed into shell

echo Done!