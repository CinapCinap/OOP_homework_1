class Track:
    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.duration = track_duration
    def show(self):
        print(f'<{self.track_name} - {self.duration} мин.>')        
class Album(Track):
    def __init__(self, band, album_name):
        self.album_name = album_name
        self.band = band
        self.track_list = []
    def get_track(self):
        print(f'Группа {self.band}, альбом {self.album_name}, список треков:')
        for elm in self.track_list:
            elm.show()                
    def add_track(self, new_track, new_duration):
        tr = Track(new_track, new_duration)
        self.track_list.append(tr)        
    def get_duration(self):
        total_duration = 0
        for elm in self.track_list:
            total_duration += elm.duration
        print(f'Длительность альбома {self.album_name} - {total_duration} мин.')        

album1 = Album('Blue Oyster Cult', 'Fire of Unknown Origin')
album1.add_track('Fire of Unknown Origin', 4)
album1.add_track('Burnin\' for You', 4)
album1.add_track('Veteran of the Psychic Wars', 5)
album1.get_track()
album1.get_duration()

album2 = Album('Imelda May', 'Love Tattoo')
album2.add_track('Big Bad Handsome Man', 3)
album2.add_track('Feel Me', 2)
album2.add_track('Smockers\' song', 2)
album2.get_track()
album2.get_duration()

