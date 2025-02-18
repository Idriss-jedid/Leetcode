import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    gbactivity = activity.groupby(["player_id"])[["event_date"]].min().reset_index()
    gbactivity.rename(columns={"event_date": "first_login"}, inplace=True)
    return gbactivity