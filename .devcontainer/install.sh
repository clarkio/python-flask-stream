# install prerequisite for pyenv
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git


# install pyenv
rm -rf ~/.pyenv

sudo curl https://pyenv.run | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# reload bashrc
source ~/.bashrc
. ~/.bashrc

# install Python 3.8.1 from pyenv
pyenv install 3.8.1

python3 -m venv venv 
# install flask

# install github hub
wget https://github.com/github/hub/releases/download/v2.13.0/hub-linux-amd64-2.13.0.tgz
tar -xf hub-linux-amd64-2.13.0.tgz
sudo ./hub-linux-amd64-2.13.0/install

#clean up hub install
rm -rf hub*

git config --global hub.protocol https