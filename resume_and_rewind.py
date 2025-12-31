class StatefulAgent:
    def __init__(self):
        self.context = []
        self.checkpoints = []

    def step(self, message):
        self.context.append(message)
        self.checkpoints.append(self.context.copy())

    def resume_from(self, index):
        self.context = self.checkpoints[index].copy()


agent = StatefulAgent()

agent.step("User goal defined")
agent.step("Constraints added")
agent.step("Plan generated")

agent.resume_from(1)

print(agent.context)
