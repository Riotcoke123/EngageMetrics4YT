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

# Fetch live stream details, including view count and engagement score
def get_live_stream_details(youtube, video_id):
    response = youtube.videos().list(
        part='snippet,liveStreamingDetails',
        id=video_id
    ).execute()

    # Extracting required details
    if response['items']:
        username = response['items'][0]['snippet']['channelTitle']
        total_viewers = int(response['items'][0]['liveStreamingDetails'].get('concurrentViewers', 0))
        engagement_score = random.uniform(0.5, 0.9)  # Placeholder for actual engagement calculation
        return username, total_viewers, engagement_score
    return None

# Reverse engineer the real viewers based on the engagement score
def estimate_real_viewers(engagement_score, total_viewers):
    """
    Reverse-engineering logic:
    - High engagement (0.8 - 1.0) -> More real viewers
    - Low engagement (0.1 - 0.4) -> More bot viewers
    """
    if engagement_score > 0.8:
        # High engagement: assume 70-90% real viewers
        real_viewers = int(total_viewers * random.uniform(0.7, 0.9))
    elif engagement_score > 0.5:
        # Medium engagement: assume 50-70% real viewers
        real_viewers = int(total_viewers * random.uniform(0.5, 0.7))
    else:
        # Low engagement: assume 30-50% real viewers
        real_viewers = int(total_viewers * random.uniform(0.3, 0.5))
    
    return real_viewers

# Estimate bot viewers based on total viewers and real viewers
def estimate_bot_viewers(total_viewers, real_viewers):
    bot_viewers = total_viewers - real_viewers
    return bot_viewers

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
    video_id = 'PQnv_meNns4'  # Replace with the actual video ID
    file_path = r'data.json'    # Specify the file path

    # Initialize YouTube API client
    youtube = initialize_youtube(api_key)

    # Fetch live stream data
    live_data = get_live_stream_details(youtube, video_id)
    if not live_data:
        logging.warning("Stream details could not be retrieved.")
        return

    username, total_viewers, engagement_score = live_data
    logging.info(f"Fetched data: Username: {username}, Total Viewers: {total_viewers}, Engagement Score: {engagement_score}")

    # Estimate real viewers based on engagement score
    real_viewers = estimate_real_viewers(engagement_score, total_viewers)

    # Estimate bot viewers
    bot_viewers = estimate_bot_viewers(total_viewers, real_viewers)

    # Prepare data for JSON output
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
