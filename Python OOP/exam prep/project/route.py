class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self._start_point

    @start_point.setter
    def start_point(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Start point cannot be empty!")
        self._start_point = value

    @property
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, value):
        value = value.strip()
        if not value:
            raise ValueError("End point cannot be empty!")
        self._end_point = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 1.00:
            raise ValueError("Length cannot be less than 1.00 kilometer!")
        self._length = value
