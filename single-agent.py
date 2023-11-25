import torch as T
import numpy as np
import matplotlib.pyplot as plt

from game import Game
from tqdm import tqdm

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


np.random.seed(1)
T.manual_seed(1)

n_episodes = 300
game_len = 10000
n_players = 8

figure_file = 'plots/score_sp.png'

game = Game(n_players)

agent = game.level.player_sprites[0].agent

score_history = np.zeros(shape=(game.max_num_players, n_episodes))
best_score = 0
avg_score = np.zeros(n_episodes)

for i in tqdm(range(n_episodes)):
    # TODO: Make game.level.reset_map() so we don't __init__ everything all the time (such a waste)
    if i != 0:
        game.level.__init__(n_players, reset=True)
    # TODO: Make game.level.reset_map() so we don't pull out and load the agent every time (There is -definitevly- a better way)

    for player in game.level.player_sprites:
        player.stats.exp = score_history[player.player_id][i-1]
        player.agent = agent

    for j in tqdm(range(game_len)):
        if not game.level.done:

            game.run()
            game.calc_score()

            for player in game.level.player_sprites:
                if player.is_dead():
                    player.kill()

            # if (j == game_len-1 or game.level.done) and game.level.enemy_sprites != []:
            #     for player in game.level.player_sprites:
            #         for enemy in game.level.enemy_sprites:
            #             player.stats.exp *= .95

    for player in game.level.player_sprites:
        exp_points = player.stats.exp
        score_history[player.player_id][i] = exp_points
        avg_score[i] = np.mean(score_history)

    if avg_score[i] >= best_score:
        print(
            f"\nNew Best score: {avg_score[i]}\
            \nOld Best score: {best_score}"
        )
        best_score = avg_score[i]
        print("Saving models for agent...")
        agent.save_models(
            actr_chkpt="player_actor", crtc_chkpt="player_critic")
        print("Models saved ...\n")
    else:
        print(
            f"Average score of round: {avg_score[i]}\
              \nBest score: {np.mean(best_score)}"
        )


print("\nEpisodes done, saving models...")
agent.save_models(
    actr_chkpt="player_actor", crtc_chkpt="player_critic")
print("Models saved ...\n")

plt.plot(avg_score)
plt.savefig(figure_file)
game.quit()

plt.show()
