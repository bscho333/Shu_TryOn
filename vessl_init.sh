# Based on Vessl Workspace

# Project root
PROJECT_ROOT=/root

pip install vessl gdown
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#sh Miniconda3-latest-Linux-x86_64.sh
vessl dataset download tps / /root/checkpoints/tps/79epoch
vessl dataset download CLIP-Embedding / /root/Shu_TryOn/ladi-vton/data
vessl dataset download inversion / /root/checkpoints/
vessl dataset download emasc / /root/checkpoints/
vessl dataset download VT-Hub / /root/VT_Hub
cd VT_Hub || return
unzip VT_Hub.zip

# For libGL.so.1 error
su -
apt-get update
apt-get install sudo -y
sudo apt-get update
apt-get -y install libgl1-mesa-glx
exit
