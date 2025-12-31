class AgentRuntimeState:
    def __init__(self):
        self.step = 0
        self.context = []

    def save(self):
        return {
            "step": self.step,
            "context": self.context.copy()
        }

    def load(self, state):
        self.step = state["step"]
        self.context = state["context"]


runtime = AgentRuntimeState()

runtime.step = 1
runtime.context.append("User wants a market analysis")

saved_state = runtime.save()

# --- Resume execution ---
new_runtime = AgentRuntimeState()
new_runtime.load(saved_state)

print(new_runtime.step)
print(new_runtime.context)
