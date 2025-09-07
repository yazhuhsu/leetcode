import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.sort_values('score',ascending=False)
    df = df.groupby('score',sort=False)['score'].count().reset_index(name='count')
    df = df.drop('count', axis=1)
    df.insert(0, 'rank', range(1, 1+len(df)))

    scores = scores.drop('id', axis=1)
    scores = scores.join(df.set_index('score'), on='score')

    return scores.sort_values('score', ascending=False)

data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.5, 3.65, 4, 3.85, 4, 3.65]
}
print(order_scores(pd.DataFrame(data=data)))