from arguments import get_args
from baselines.common.atari_wrappers import make_atari
from baselines import bench
from baselines import logger
from baselines.common.atari_wrappers import wrap_deepmind
from agent import agent
import os 

if __name__ == '__main__':
    if not os.path.exists('logs/'):
        os.mkdir('logs/')
    envArgs = get_args()
    log_path = 'logs/' + envArgs.env_name + '/'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logger.configure(log_path)
    # start to create the environment
    environment = make_atari(envArgs.env_name)
    environment = bench.Monitor(environment, logger.get_dir())
    environment = wrap_deepmind(environment, frame_stack=True)
    trainer = agent(environment, envArgs)
    trainer.learn()
    environment.close()
