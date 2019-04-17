# AI-Assignment2

This repo is for CS7IS2 Artificial Intelligence Assignment 2 - Group Project.

Environment Requirements:
-------------------------
python-3.5.2 <br>
openai-gym <br>
pytorch-0.4.0<br>
openai-baselines<br>
mujoco-py-1.50.1.56<br>

Installation:
-------------
1.install openai-baselines <br>
git clone https://github.com/openai/baselines.git<br>
cd baselines<br>
pip install -e .<br>
2.install grm[atari]<br>
pip install 'gym[atari]'<br>
3.install pytorch<br>
pip3 install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp35-cp35m-win_amd64.whl<br>
pip3 install torchvision<br>

Instructions:
-------------
1.select a training algorithm<br>
cd [algorithm folder] <br>
2. train the networks<br>
command example<br>
python train_DQN.py --env-name=KangarooNoFrameskip-v4 --cuda<br>
