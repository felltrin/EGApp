import pandas as pd

def load_data():
    match_game_state = pd.read_parquet('data/game_state_frame_data.parquet', engine='pyarrow')
    return match_game_state
