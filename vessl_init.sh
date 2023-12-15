# Based on Vessl Workspace

pip install git gdown vessl
git clone https://github.com/bscho333/Shu_TryOn.git
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#sh Miniconda3-latest-Linux-x86_64.sh
vessl dataset download tps / /root/tps/79epoch
vessl dataset download CLIP-Embedding / /root/Shu_TryOn/ladi-vton/data
vessl dataset download inversion / /root/
vessl dataset download emasc / /root/
vessl dataset download VT-Hub / /root/VT_Hub
cd VT_Hub || return
unzip VT_Hub.zip