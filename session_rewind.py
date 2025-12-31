class RewindableSession:
    def __init__(self):
        self.history = []
        self.snapshots = []

    def add(self, message):
        self.history.append(message)
        self.snapshots.append(self.history.copy())

    def rewind(self, index):
        self.history = self.snapshots[index].copy()


session = RewindableSession()

session.add("User asks for business plan")
session.add("Agent proposes cafe")
session.add("User changes budget")

session.rewind(1)

print(session.history)
