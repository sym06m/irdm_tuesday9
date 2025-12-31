class Agent:
    def __init__(self):
        self.session = []

    def respond(self, text):
        self.session.append(text)
        return f"Agent response to: {text}"

    def rewind(self, step):
        self.session = self.session[:step]


agent = Agent()

agent.respond("Open a shop")
agent.respond("Choose location")
agent.respond("Estimate costs")

agent.rewind(2)

print(agent.session)
