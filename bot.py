import json
import random
import logging
import os
from googleapiclient.discovery import build

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def initialize_youtube(api_key):
    """Initialize YouTube API client."""
    if not api_key:
        logging.error("API key is missing.")
        raise ValueError("API key is missing.")
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
    except Exception as e:
        logging.error(f"Error initializing YouTube client: {e}")
        raise

def estimate_bot_viewers(total_viewers, engagement_score):
    """
    Estimate the number of bot viewers based on total viewers and engagement score.
    Bots are likely to be higher when the engagement score is lower.
    """
    # Lower engagement often correlates with more bots
    bot_percentage = 0.05 + (1 - engagement_score) * 0.4  # Bots rise as engagement decreases
    bot_viewers = int(total_viewers * bot_percentage)

    # Cap bot viewers to ensure it doesn't exceed total viewers
    bot_viewers = min(bot_viewers, total_viewers)

    return bot_viewers

def estimate_real_viewers(total_viewers, bot_viewers):
    """
    Estimate real viewers as the remaining viewers after accounting for bots.
    """
    return total_viewers - bot_viewers

def main():
    # Your API key
    api_key = ''  # Replace with your API key
    video_id = 'nNCIcA-bras'  # Replace with your video ID
    file_path = r'data.json'  # Specify where to save the output

    try:
        logging.info("Starting script...")

        # Initialize YouTube API client
        youtube = initialize_youtube(api_key)

        # Fetch live stream data
        response = youtube.videos().list(
            part='snippet,liveStreamingDetails',
            id=video_id
        ).execute()

        if response.get('items'):
            video_details = response['items'][0]
            username = video_details['snippet']['channelTitle']
            total_viewers = int(video_details['liveStreamingDetails'].get('concurrentViewers', 0))
            engagement_score = random.uniform(0.3, 0.5)  # Placeholder for now

            # Estimate bot and real viewers based on engagement score and total viewers
            bot_viewers = estimate_bot_viewers(total_viewers, engagement_score)
            real_viewers = estimate_real_viewers(total_viewers, bot_viewers)

            # Prepare data
            data = {
                "username": username,
                "total_viewers": total_viewers,
                "engagement_score": engagement_score,
                "real_viewers": real_viewers,
                "bot_viewers": bot_viewers
            }

            # Save to JSON
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Data saved to {file_path}")
            print(f"Data saved to {file_path}")
        else:
            logging.warning("No data found for the provided video ID.")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
