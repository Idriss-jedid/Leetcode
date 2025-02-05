import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    gb = actor_director.groupby(["actor_id", "director_id"])[["timestamp"]].count().reset_index()
    return gb[gb["timestamp"] >= 3][["actor_id", "director_id"]]