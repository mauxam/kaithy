"""
Environment have adverarial property
This environment have 1 opponent agent only
"""
import gym
from . import gym_gomoku


class AdversarialEnv:
    def __init__(self, environment_id, opponent_policy):
        self.env = gym.make(environment_id)
        self._opponent_policy = opponent_policy

        self.reset()

    @property
    def opponent_policy(self):
        return self._opponent_policy

    @opponent_policy.setter
    def opponent_policy(self, opponent_policy):
        self._opponent_policy = opponent_policy

    def step(self, action):
        return self.env.step(action)

    def reset(self):
        # A trick
        # Reset env and attach defined opponent policy to env
        return self.env.step(self.opponent_policy)

    def render(self):
        return self.env.render()

    @property
    def action_space(self):
        return self.env.action_space

    @property
    def observation_space(self):
        return self.env.observation_space
