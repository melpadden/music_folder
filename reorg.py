folders = []
artists = {}
albums = {}
root_directory = "/media/mel/8376-25E2"
import os




def store_tree():
    """Store all the artists in the folder"""
    artists.clear()
    for artist_entry in os.scandir(root_directory):
        if artist_entry.is_file(): continue
        artist_albums = []
        artist_dir = os.path.join(root_directory, artist_entry)
        for album_entry in os.scandir(artist_dir):
            if album_entry.is_file(): continue
            album = []
            for song_entry in os.scandir(os.path.join(artist_dir, album_entry)):
                if song_entry.is_file():
                    album.append(song_entry)
            albums[album_entry] = album
            artist_albums.append(album_entry)
        artists[artist_entry] = artist_albums

def generate_list():
    """
        generate a songlist.json describing the contents of the folder
    """
    pass

def main():
    store_tree()
    for artist_key in artists.keys():
        print(artist_key)
        print(f"\t{artists[artist_key]}")
        

if  __name__ == "__main__":
    main()