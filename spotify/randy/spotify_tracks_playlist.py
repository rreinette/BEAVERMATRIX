import spotipy
import spotipy.util as util
import json

def get_tracks_id(uri,sp):
	track_id_uris = []
	username = uri.split(':')[2]
	playlist_id = uri.split(':')[4]
	results = sp.user_playlist(username, playlist_id)
	for song in results['tracks']['items']:
		track_id_uris.append(song['track']['id'])


	print(str(track_id_uris))

def get_featured_playlists_uris(name, sp):
	response = sp.featured_playlists()
	print(response['message'])
	uri = ''

	while response:
		playlists = response['playlists']
		for i, item in enumerate(playlists['items']):
			if item['name'] == name:
				uri = item['uri']
		if playlists['next']:
			response = sp.next(playlists)
		else:
			response = None
	return uri
def main():
	client_id = "ae2a0a93e2594654bd054f108664a9de"
	client_secret = "15d598eed3ea4f5b8ac76c63adb0eee5"
	username = '11173741361'
	token = util.prompt_for_user_token(username,scope="user-read-private", client_id = client_id, client_secret = client_secret, redirect_uri='http://localhost:8080')
	sp = spotipy.Spotify(auth=token)
	uri = get_featured_playlists_uris('Today\'s Top Hits',sp)
	get_tracks_id(uri,sp)
if __name__ == '__main__':
	main()


