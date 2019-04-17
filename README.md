# AI-Assignment2

This repo is for CS7IS2 Artificial Intelligence Assignment 2 - Group Project.

Environment Requirements:
python-3.5.2
openai-gym
pytorch-0.4.0
openai-baselines
mujoco-py-1.50.1.56

Installation:
1.install openai-baselines 
git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .
2.install grm[atari]
pip install 'gym[atari]'
3.install pytorch
pip3 install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp35-cp35m-win_amd64.whl
pip3 install torchvision

Instructions:
1.select a training algorithm
cd <algorithm folder>
2. train the networks
command example
python train_DQN.py --env-name=KangarooNoFrameskip-v4 --cuda
