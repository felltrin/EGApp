import pandas as pd
import numpy as np


class ProcessGameState:
    def __init__(self):
        self.weapon_classes = None
        self.game_state = pd.read_parquet('data/game_state_frame_data.parquet', engine='pyarrow')
        self.inventory_class = pd.DataFrame()
        self.coord_processed = pd.DataFrame()


    def is_within_quadrilateral(self, point, A, B, C, D):
        x, y = point

        # Calculate the equations of the sides
        eq_AB = lambda x, y: (B[1] - A[1]) * (x - A[0]) - (B[0] - A[0]) * (y - A[1])
        eq_BC = lambda x, y: (C[1] - B[1]) * (x - B[0]) - (C[0] - B[0]) * (y - B[1])
        eq_CD = lambda x, y: (D[1] - C[1]) * (x - C[0]) - (D[0] - C[0]) * (y - C[1])
        eq_DA = lambda x, y: (A[1] - D[1]) * (x - D[0]) - (A[0] - D[0]) * (y - D[1])

        # Check if the point satisfies the inequalities for all sides
        if eq_AB(x, y) >= 0 and eq_BC(x, y) >= 0 and eq_CD(x, y) >= 0 and eq_DA(x, y) >= 0:
            return True
        else:
            return False


    def process_coord_boundary(self):
        self.game_state = self.game_state.loc[(self.game_state['z'] >= 285) & (self.game_state['z'] <= 421)]
        # self.game_state.reset_index(inplace=True)
        for index, row in self.game_state.iterrows():
            A = (-2806, 742)
            B = (-2472, 1233)
            C = (-1565, 580)
            D = (-1735, 250)
            point = row[['x', 'y']]

            if self.is_within_quadrilateral(point, A, B, C, D):
                self.coord_processed = self.coord_processed._append(row)


    def process_inventory_classes(self):
        for index, row in self.coord_processed.iterrows():
            json_objects = []
            for dict in row['inventory']:
                json_objects.append(dict)

            if index == 0:
                self.inventory_class = pd.DataFrame(json_objects)
            else:
                self.inventory_class = self.inventory_class._append(json_objects, ignore_index=True)

        self.weapon_classes = np.array(self.inventory_class['weapon_class'].values)


    def print_the_data(self):
        team_2_data_t = self.coord_processed.loc[
            (self.coord_processed['team'] == "Team2") & (self.coord_processed['side'] == "T")]
        team_2_data_ct = self.coord_processed.loc[
            (self.coord_processed['team'] == "Team2") & (self.coord_processed['side'] == "CT")]
        print("Values for team 2 ct side")
        print(team_2_data_ct[['area_name', 'side']].head(10))
        print("\n")
        print("Values for team 2 t side")
        print(team_2_data_t[['clock_time', 'seconds', 'side']].head(10))
        print("\n")
