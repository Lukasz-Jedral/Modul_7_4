class Movie():
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre

        #Variables
        self._views = 0

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    def __repr__(self):
        return f'{self.title} ({self.release_year})'

    def views_number(self,number):
        self._views = number
        return self._views

    def play(self):
        self._views += 1


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season= season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{int(self.season):02d}E{int(self.episode):02d}'

    def __repr__(self):
        return f'{self.title} S{int(self.season):02d}E{int(self.episode):02d}'
