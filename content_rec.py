import pandas as pd
from scipy.spatial import distance
import time

pd.set_option('display.max_colwidth', 10000)
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', 10000)


def get_submission_target(df):
    """Identify target rows with missing click outs."""

    mask = df["reference"].isnull() & (df["action_type"] == "clickout item")
    df_out = df[mask]
    del df_out['action_type']
    del df_out['reference']
    del df_out['platform']
    del df_out['city']
    del df_out['device']
    del df_out['current_filters']
    del df_out['prices']
    return df_out


print(f"Reading test.csv ...")
t1 = time.time()
df_test = pd.read_csv('C:\\Users\\banana\\PycharmProjects\\trivago\\data\\test.csv')
print("Identify target rows...")
df_target = get_submission_target(df_test)
t2 = time.time()
print('Done: ' + str(t2 - t1))

for index, row in df_target.iterrows():
    user = row['user_id']
    user_vector = ...  # TODO
    impressions = row['impressions'].strip('\n').split('|')
    for i in range(len(impressions)):
        # TODO make sure these are compatible for the cosine distance
        item_vector = ...  # TODO
        impressions[i] = distance.cosine(item_vector, user_vector)
    impressions.sort()
    sp = ' '
    df_target.at[user, 'impressions'] = sp.join(impressions)  # String of the ordered impressions

# Find all users with click-out interactions
# For each user
#     For each impression calculate the cosine similarity between item profile vector & user profile vector
#     Rank impressions most similar to least

