class Room:
    def __init__(self, name, capacity, songs, guests, till):
        self.name = name
        self.capacity = capacity
        self.songs = songs
        self.guests = guests
        self.till = till

    def add_song_to_room(self, room, song):
        self.songs.append(song)
        return(self.songs)

    def find_song_in_room_by_title(self, title):
        for song in self.songs:
            if song.title == title:
                return song.title

    def song_in_room(self, song):
        if song in self.songs:
            return True
        else:
            return False

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
        return self.guests

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)
        return self.guests 

    def check_capacity_before_entry(self, guest):
        if self.capacity <= len(self.guests):
            return "Room is full sorry!"
        elif self.capacity > len(self.guests):
             self.add_guest_to_room(guest)

    def charge_guest_entry_fee(self, guest, fee):
        guest.purse -= fee

    def add_fee_to_room_till(self, fee):
        self.till += fee
        


        
