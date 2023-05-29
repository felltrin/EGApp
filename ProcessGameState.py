import pandas as pd
import numpy as np
import json


class ProcessGameState:
    def __init__(self):
        self.weapon_classes = None
        self.game_state = pd.read_parquet('data/game_state_frame_data.parquet', engine='pyarrow')
        self.inventory_class = pd.DataFrame()


    def process_coord_boundary(self):
        self.game_state = self.game_state.loc[(self.game_state['z'] >= 285) & (self.game_state['z'] <= 421)]
        self.game_state = self.game_state.loc[(self.game_state['y'] >= 250) & (self.game_state['y'] <= 1233)]
        self.game_state = self.game_state.loc[(self.game_state['x'] >= -2806) & (self.game_state['x'] <= -1565)]
        self.game_state.reset_index(inplace=True)


    def process_inventory_classes(self):
        for index, row in self.game_state.iterrows():
            json_objects = []
            for dict in row['inventory']:
                json_objects.append(dict)

            if index == 0:
                self.inventory_class = pd.DataFrame(json_objects)
            else:
                self.inventory_class = self.inventory_class._append(json_objects, ignore_index=True)

        self.weapon_classes = self.inventory_class['weapon_class'].values


"""
TO-DO: REMOVE ONCE FINISHED
NOTES:
X_LABEL, Y_LABEL, Z_LABEL = 'x', 'y', 'z'
FIRST_INDICE, FIFTH_INDICE = 0, 5
TENTH_INDEX = 10
print(game_state[[X_LABEL, Y_LABEL, Z_LABEL]][FIRST_INDICE:TENTH_INDEX])
print(game_state.loc[0])
print(game_state['inventory'][0])
inventory_curr = game_state['inventory'][0][0]
print(inventory_curr)

print(game_state['player'][0:100])
print(game_state.loc[3])
for index, row in game_state.iterrows():
    print(index, row['inventory'])
print(game_state['y'][0:5])
print(game_state.columns)
for getting the column of player 4
game_state.loc[game_state['player'] == 'Player4']
"""