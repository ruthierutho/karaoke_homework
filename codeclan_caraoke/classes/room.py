class Room:
    def __init__(self, name, capacity, songs):
        self.name = name
        self.capacity = capacity
        self.songs = []

    def add_song_to_room(self, room, song):
        self.songs += song
        return self.songs

        
