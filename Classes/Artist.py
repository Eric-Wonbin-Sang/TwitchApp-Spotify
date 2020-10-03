
class Artist:

    def __init__(self, **kwargs):

        self.name = kwargs["name"]
        self.id = kwargs["id"]
        self.spotify_link = kwargs["external_urls"]["spotify"]

    def __str__(self):
        return "Artist: {}, id: {}".format(
            self.name,
            self.id
        )
