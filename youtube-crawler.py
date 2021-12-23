from youtube_dl import YoutubeDL
import boto3


def search_download(search_str, search_results):

    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        videos = ydl.extract_info(f"ytsearch{search_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos]


if __name__ == '__main__':
    # TODO you can change to any search string you want
    downloaded_files = search_download('polyphia - goat', 5)

    # TODO use downloaded_files and complete a few lines to upload them to an S3 bucket
    s3_client = boto3.client('s3')
    s3_client.upload_file('downloaded_files', 'Need to create a bucket', 'youtubeFiles')
