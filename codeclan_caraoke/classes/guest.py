class Guest:
    def __init__(self, name, favourite_song, purse):
        self.name = name
        self.favourite_song = favourite_song
        self.purse = purse

    def guest_react_to_fave_song(self, room):
        for song in room.songs:
            if self.favourite_song in song.title:
                return "Yassss put it on! I know allll the words!!"
        else:
            return "Booooooo that's rubbish"
