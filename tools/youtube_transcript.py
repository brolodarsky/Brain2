from asyncio import DatagramTransport
import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi()
        transcript = transcript_list.fetch(video_id)
        # transcript_text = "\n".join([item['text'] for item in transcript_list])
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_transcript.py <youtube_url_or_id> [output_file]")
        sys.exit(1)
        
    url_or_id = sys.argv[1]
    video_id = extract_video_id(url_or_id)
    
    transcript = get_transcript(video_id)

    if transcript:
        output_file = sys.argv[2] if len(sys.argv) > 2 else f"{video_id}_transcript.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            for snippet in transcript:
                f.write(snippet.text + "\n")
        print(f"Transcript saved to {output_file}")
