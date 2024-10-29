from googleapiclient.discovery import build
import random
import json

# Initialize the YouTube API client
def initialize_youtube(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube

# Fetch live stream details, including view count and chat messages
def get_live_stream_details(youtube, video_id):
    response = youtube.videos().list(
        part='snippet,liveStreamingDetails',
        id=video_id
    ).execute()

    # Extracting required details
    if response['items']:
        title = response['items'][0]['snippet']['title']
        username = response['items'][0]['snippet']['channelTitle']
        total_viewers = int(response['items'][0]['liveStreamingDetails']['concurrentViewers'])

        return username, title, total_viewers
    return None

# Estimate bot viewers using basic engagement-based approximation
def estimate_bot_viewers(total_viewers, engagement_score):
    bot_viewers = total_viewers * (1 - engagement_score)  # engagement score (0-1) is a rough measure of real views
    real_viewers = total_viewers - bot_viewers
    return int(bot_viewers), int(real_viewers)

# Save data to JSON
def save_to_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Main function to execute
def main():
    api_key = ''
    video_id = 'BIy5z1TVGhM'  # Replace with actual video ID
    file_path = r'data.json'

    # Initialize YouTube API client
    youtube = initialize_youtube(api_key)

    # Fetch live stream data
    live_data = get_live_stream_details(youtube, video_id)
    if not live_data:
        print("Stream details could not be retrieved.")
        return

    username, title, total_viewers = live_data

    # Simulate engagement score based on arbitrary chat and like ratios as a placeholder
    engagement_score = random.uniform(0.5, 0.9)  # Placeholder for real engagement ratio based on chat analysis

    # Calculate bot and real viewers
    bot_viewers, real_viewers = estimate_bot_viewers(total_viewers, engagement_score)

    # Prepare data for JSON output
    data = {
        "username": username,
        "total_viewers": total_viewers,
        "bot_viewers": bot_viewers,
        "real_viewers": real_viewers
    }

    # Save data to JSON
    save_to_json(data, file_path)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    main()
