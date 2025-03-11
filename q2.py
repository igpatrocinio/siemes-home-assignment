# Question 2 (code required):
# Write a small application to print out the IDs of the 2 users who logged in at the closest time to each other, along with the times of login. These should be the two users with the closest login times of all the users in the data set.

# Again, we are not looking for the most optimal code, but a variety of plausible approaches.

import json
import pandas as pd

def main():

    with open('records.json', 'r') as f:
        contents = f.read()

    # reading the contents as a json object
    json_contents = json.loads(contents)

    # converting the json to a dataframe
    df = pd.DataFrame(json_contents)

    # converting the last_login to a datetime object
    df["last_login"] = pd.to_datetime(df["last_login"])

    # sorting the df by the time_login column
    sorted_df = df.sort_values(by="last_login").reset_index(drop=True)

    # creating the lagged last login and user
    sorted_df["previous_last_user"] = sorted_df["id"].shift(1)
    sorted_df["previous_last_login"] = sorted_df["last_login"].shift(1)

    # creating difference column, between the last user login and the previous one
    sorted_df["diff"] = sorted_df["previous_last_login"] - sorted_df["last_login"]
    sorted_df["diff"] = abs(sorted_df["diff"].dt.total_seconds())

    # getting the smallest difference between the current user and previous one
    final_df = sorted_df.sort_values(by="diff").head(1)

    # renaming the columns for a friendlier name
    final_df.rename(columns={'id': 'user1', 'previous_last_user': 'user2'}, inplace=True)

    print(f"The 2 users who logged in at the closest time to each other:\n{final_df[['user1', 'user2']].to_string(index=False)}")


if __name__ == '__main__':
    main()