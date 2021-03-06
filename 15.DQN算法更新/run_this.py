from maze_env import Maze
from RL_brain import DeepQNetwork

def run_maze():
    step = 0  # 记录走到了第几步，当step较小时，不进行学习，而是形成一个记忆库
    for episode in range(300):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # 存储记忆的一个步骤，
            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    # maze game
    env = Maze()
    RL = DeepQNetwork(env.n_actions, env.n_features,
    learning_rate=0.01,
    reward_decay=0.9,
    e_greedy=0.9,
    replace_target_iter=200,
    memory_size=2000,
    output_graph=True   # 是否输出图像，True or False
    )

    env.after(100, run_maze)
    env.mainloop()
    RL.plot_cost()

# VS Code中直接调用tensorboard的方法。
# https://devblogs.microsoft.com/python/python-in-visual-studio-code-february-2021-release/