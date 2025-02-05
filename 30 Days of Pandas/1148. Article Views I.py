import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result_series = views[views['author_id'] == views['viewer_id']]['author_id'].drop_duplicates().sort_values().rename('id')
    result_df = pd.DataFrame(result_series)
    return result_df