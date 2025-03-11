# Question 1 (code required):
# Write a small application to print out the IDs of the 3 users with logins closest to 2025-02-01 00:00 UTC. Your result should be the ones closest in absolute terms, that is, either before or after that date.

# We are not looking for the most optimal code, but a variety of methods you could use calculate the smallest difference and why you would select one method over another.

# Final Answer: For small datasets any of them will perform the same. But for larger dataset Pandas will perform better as it was built on top of numpy and
# is more suited for bulk operations

import json
import pandas as pd
from datetime import datetime

def main1():

    try:
        with open('records.json', 'r') as f:
            contents = f.read()
        try:
            # reading the contents as a json object
            json_contents = json.loads(contents)
        except json.JSONDecodeError:
            print("JSON file is not able to be properly read. Please fix the malformed strings and try it again")
        

        # converting the json to a dataframe
        df = pd.DataFrame(json_contents)

        # converting the last_login to a datetime object
        df["last_login"] = pd.to_datetime(df["last_login"])

        # creating the the time difference column and it to seconds in absolute values
        df["diff"] = pd.to_datetime("2025-02-01 00:00+00:00") - df["last_login"]
        df["diff"] = abs(df["diff"].dt.total_seconds())

        # sorting the df by the time difference column
        sorted_df = df.sort_values(by="diff")

        # getting the top 3 ids
        final_df = sorted_df["id"].head(3)

        print(f"the top 3 users who logged in closer to Feb 1st are:\n{final_df.to_string(index=False)}")
    
    except FileNotFoundError:
        print("The file was not found. Please add it or rename it.")


def main2():
    # reading the contents as a json objec
    try:
        with open('records.json', 'r') as f:
            contents = f.read()
        try:
            # reading the contents as a json object
            json_contents = json.loads(contents)
        except json.JSONDecodeError:
            print("JSON file is not able to be properly read. Please fix the malformed strings and try it again")
    # converting the last_login column to datetime and calculate the difference

        json_contents = json.loads(contents)

        for record in json_contents:
            record["last_login"] = datetime.strptime(record["last_login"], "%Y-%m-%dT%H:%M:%SZ")
            record["diff"] = abs(record["last_login"] - datetime.fromisoformat("2025-02-01 00:00"))
        
        json_contents_sorted = sorted(
            json_contents,
            key=lambda record: record["diff"].total_seconds()
        )

        json_contents_final = [record["id"] for record in json_contents_sorted[0:3]]

        print(f"the top 3 users who logged in closer to Feb 1st are:\n{json_contents_final}")

    except FileNotFoundError:
        print("The file was not found. Please add it or rename it.")

if __name__ == '__main__':
    main1()