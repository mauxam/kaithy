import sys
sys.path.append('..')

import numpy as np

import adversarial_gym as gym
from baselines import deepq


def val_opponent_policy(curr_state, prev_state, prev_action):
    '''
    Define policy for opponent to validate model here
    '''
    return gym.gym_gomoku.envs.util.make_beginner_policy(np.random)(curr_state, prev_state, prev_action)


def main():
    env = gym.make('Gomoku5x5-training-camp-v0')
    val_env = gym.make('Gomoku5x5-training-camp-v0', val_opponent_policy)
    # Enabling layer_norm here is import for parameter space noise!
    model = deepq.models.cnn_to_mlp(
        convs=[(64, 3, 1), (64, 3, 1), (64, 3, 1), (64, 3, 1),
               (64, 3, 1), (64, 3, 1), (64, 3, 1), (64, 3, 1)],
        hiddens=[64]
    )
    act = deepq.learn(
        env=env,
        val_env=val_env,
        q_func=model,
        lr=1e-4,
        max_timesteps=int(sys.argv[1]),
        buffer_size=10000,
        batch_size=32,
        exploration_fraction=0.95,
        exploration_final_eps=0.01,
        train_freq=1,
        val_freq=1000,
        print_freq=100,
        learning_starts=1000,
        target_network_update_freq=1000,
        gamma=0.99,
        prioritized_replay=True,
        deterministic_filter=True,
        random_filter=True,
    )
    print("Saving model to kaithy_cnn_to_mlp_5_model.pkl")
    act.save("kaithy_cnn_to_mlp_5_model.pkl")


if __name__ == '__main__':
    main()