class Process:
    """
        class for process in which we store:

        -name of the process,
        -its priority
        -time slices needed to complete its task
    """

    __slots__ = "name", "priority", "timeSlices"

    def __init__(self, name: str, priority: int, timeSlices: int):
        self.name = name
        self.priority = priority
        self.timeSlices = timeSlices
