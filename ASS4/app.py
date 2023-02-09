import gym
import os
import matplotlib.pyplot as plt
import numpy as np
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1400, 900))
display.start()


# %matplotlib inline


if type(os.environ.get("DISPLAY")) is not str or len(os.environ.get("DISPLAY")) == 0:
    # !bash ../xvfb start
    # %env  Display=:1
    
import gym
env = gym.make("CartPole-v0")
x = env.reset()

plt.imshow(env.render("rgb_array"))
print("Observation space", env.observation_space)
