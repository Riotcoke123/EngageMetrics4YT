from googleapiclient.discovery import build
import random
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the YouTube API client
def initialize_youtube(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube

# Fetch live stream details, including view count
def get_live_stream_details(youtube, video_id):
    response = youtube.videos().list(
        part='snippet,liveStreamingDetails',
        id=video_id
    ).execute()

    # Extracting required details
    if response['items']:
        username = response['items'][0]['snippet']['channelTitle']
        total_viewers = int(response['items'][0]['liveStreamingDetails'].get('concurrentViewers', 0))
        return username, total_viewers
    return None

# Calculate engagement score based on chat analysis (placeholder for real chat analysis)
def calculate_engagement_score(youtube, video_id):
    try:
        # For now, using random score; in practice, fetch and analyze chat messages
        engagement_score = random.uniform(0.5, 0.9)  # This should be based on actual chat analysis
        return engagement_score
    except Exception as e:
        logging.error(f"Error calculating engagement score: {e}")
        return 0.7  # Default score in case of an error

# Estimate bot viewers using basic engagement-based approximation
def estimate_bot_viewers(total_viewers, engagement_score):
    bot_viewers = total_viewers * (1 - engagement_score)  # engagement score (0-1) is a rough measure of real views
    real_viewers = total_viewers - bot_viewers
    return int(bot_viewers), int(real_viewers)

# Save data to JSON
def save_to_json(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data to JSON: {e}")

# Main function to execute
def main():
    api_key = ''  # Ensure to keep your API key secure
    video_id = 'BIy5z1TVGhM'  # Replace with actual video ID
    file_path = r'data.json'

    # Initialize YouTube API client
    youtube = initialize_youtube(api_key)

    # Fetch live stream data
    live_data = get_live_stream_details(youtube, video_id)
    if not live_data:
        logging.warning("Stream details could not be retrieved.")
        return

    username, total_viewers = live_data
    logging.info(f"Fetched data: Username: {username}, Total Viewers: {total_viewers}")

    # Calculate engagement score based on chat analysis
    engagement_score = calculate_engagement_score(youtube, video_id)

    # Calculate bot and real viewers
    bot_viewers, real_viewers = estimate_bot_viewers(total_viewers, engagement_score)

    # Prepare data for JSON output without the title
    data = {
        "username": username,
        "total_viewers": total_viewers,
        "engagement_score": engagement_score,
        "bot_viewers": bot_viewers,
        "real_viewers": real_viewers
    }

    # Save data to JSON
    save_to_json(data, file_path)

if __name__ == "__main__":
    main()
