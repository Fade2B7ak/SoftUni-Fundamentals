class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = ''
        self.longitude = ''

    def set_latitude(self, latitude):
        self.latitude = latitude
        return latitude

    def set_longitude(self, longitude):
        self.longitude = longitude
        return longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


