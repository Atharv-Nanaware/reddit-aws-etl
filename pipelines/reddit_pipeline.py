# This are the Steps that we arte taking In this pipeline;
                # Connecting to the reddit Instance
                # Extracting the Data
                # transformation Of That data
                # Loading That Tranformned Data Into a CSV File
                #( Loading That Tranformned Data Into a Database)
                
import pandas as pd                
from etls.reddit_etl import connect_reddit ,extract_posts,transform_data,load_data_to_csv
from utils.constants import SECRET,CLIENT_ID,INPUT_PATH,OUTPUT_PATH



def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    try:
        instance = connect_reddit(CLIENT_ID, SECRET, "My_Project_Atharv01")

        # Extraction
        posts = extract_posts(instance, subreddit, time_filter, limit)
        post_df = pd.DataFrame(posts)

        # Transformation
        posts_df = transform_data(post_df)

        # Loading
        file_path = f'{OUTPUT_PATH}/{file_name}.csv'
        load_data_to_csv(posts_df, file_path)
        return file_path
    except Exception as e:
        print(f"Error in reddit_pipeline: {e}")
        raise
