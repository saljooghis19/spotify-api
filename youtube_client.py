
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors



class YoutubeClient(object):
    def __init__(self):
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

        def main():
            # Disable OAuthlib's HTTPS verification when running locally.
            # *DO NOT* leave this option enabled in production.
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

            api_service_name = "youtube"
            api_version = "v3"
            client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

            # Get credentials and create an API client
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials = flow.run_console()
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, credentials=credentials)

            request = youtube.videos().update(
                part="snippet.contentDetails",
                body={
                    "id": ""
                }
            )
            response = request.execute()

            print(response)

        pass

    def get_playlist(self):
        pass

    def get_videos_from_playlist(self, playlist_id):
        pass


    def get_artist_and_track_from_video(self, video_id):
        pass

