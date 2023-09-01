import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    if scores.empty:
        return pd.DataFrame({'score' : [], 'rank' : []})
        
    scores.sort_values(by='score', ascending=False, inplace=True)
    scores.reset_index(inplace=True, drop=True)

    rank = 1
    ranks = [1]

    for i in range(len(scores)-1):
        
        if scores['score'][i] == scores['score'][i+1]:
            ranks.append(rank)
        else:
            rank+=1
            ranks.append(rank)

    scores['rank']=ranks
    scores.drop('id', axis=1, inplace=True)

    return scores