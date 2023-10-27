import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
import os
import time
import random
import shutil


'''
Original script by Dave Shapiro https://github.com/daveshap/YouTubeChapterGenerator, edits, tweaks, and additions my own.
'''


def scrape_videos(
  the_channel_url = 'https://www.youtube.com/@MrBeast',
  sorted_by = 'oldest'
  ):
  """
  Scrape transcripts from a YouTube channel by processing the videos by a    specified order.

  Parameters:
      the_channel_url (str): The URL of the YouTube channel to scrape.
      sorted_by (str): The order in which to process the videos. Can be          'newest', 'oldest', or 'popular'.

  Returns:
      None
  """
  
  def save_file(filepath, content):
      with open(filepath, 'w', encoding='utf-8') as outfile:
          outfile.write(content)
  
  
  def clean_title(title):
      contraband = [':','/','\\','?','"']
      for c in contraband:
          title = title.replace(c,'')
      return title
  
  
  videos = scrapetube.get_channel(channel_url=the_channel_url,sleep=1,sort_by=sorted_by)
  print(videos)
  
  # Check if transcripts folder exists, create it if not
  if not os.path.exists('transcripts'):
      os.makedirs('transcripts')

  
  for video in videos:
      try:
          #print(video['title'])
          #print(video)
          transcript = YouTubeTranscriptApi.get_transcript(video['videoId'])
          text = [i['text'] for i in transcript]
          block = ' '.join(text)
          title = clean_title(video['title']['runs'][0]['text'])
          print(title)
          save_file('transcripts/%s.txt' % title, block)
          time.sleep(random.randint(10,30)) #slowing down to prevent blockage
      except Exception as oops:
          print(video['title'], oops)
  
  
if __name__ == '__main__':
  scrape_videos()
  