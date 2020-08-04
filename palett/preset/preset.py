class Preset:
    max: str
    min: str
    na: str

    def __init__(self, max: str, min: str, na: str):
        self.max = max
        self.min = min
        self.na = na
