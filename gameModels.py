enemies = {}

journeys = {}

bonds = {}

vows = {}

progressByRank = {
    "troublesome": 3,
    "dangerous": 2,
    "formidible": 1,
    "extreme": 0.5,
    "epic": 0.25
}

inflictByRank = {
    "troublesome": 1,
    "dangerous": 2,
    "formidible": 3,
    "extreme": 4,
    "epic": 5
}

class Progress:
    def __init__(self, rank, progressThisRank, inflictThisRank):
        self.rank = rank
        self.progress = 0
        self.progressIncrement = progressThisRank
        self.inflictIncrement = inflictThisRank
  
    def oneProgress(self):
        self.progress += self.progressIncrement

