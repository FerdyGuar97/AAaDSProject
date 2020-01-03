class Process:

    __slots__ = "name", "priority", "timeSlices"

    def __init__(self, name: str, priority: int, timeSlices: int):
        self.name=name
        self.priority=priority
        self.timeSlices=timeSlices