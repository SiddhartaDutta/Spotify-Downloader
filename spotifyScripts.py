import spotipy

def get_playlist_ids(self, username, playlist_id):
    """
    Returns object of ids for a given playlist.
    """

    r = self.user_playlist_tracks(username,playlist_id)
    t = r['items']
    ids = []
    while r['next']:
        r = self.next(r)
        t.extend(r['items'])
    for s in t: ids.append(s["track"]["id"])
    return ids

def get_playlist_length(self, playlistId):
    """
    Takes a Spotify playlist ID and returns the playlist's length.
    """

    playlist = self.playlist_items(playlist_id=playlistId, offset=0, fields='items.track.id,total', additional_types=['track'])
    return playlist['total']
    
    # offset = 0
    # while offset != -1:
    #     response = sp.playlist_items(playlist_id, offset=0, fields='items.track.id,total', additional_types=['track'])

    #     if len(response['items']) == 0:
    #         break

    #     print(response['items'])
    #     offset = offset + len(response['items'])
    #     print(offset, "/", response['total'])

    #     if offset == response['total']:
    #         offset = -1

def get_track_info(self, songID):
    """
    Returns track info for a given track ID.
    """

    urn = 'spotify:track:' + songID
    return self.track(urn)

# new method for outputting new track names with artists (from end of main.py)