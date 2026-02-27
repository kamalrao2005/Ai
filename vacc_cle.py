import itertools

class VacuumEnvironment:
    def __init__(self, loc, A, B):
        self.agent_location = loc
        self.rooms = {'A': A, 'B': B}
        self.performance = 0

    def update(self, action):
        if action == "Suck":
            self.rooms[self.agent_location] = "Clean"
            self.performance -= 1
        elif action in ("MoveRight", "MoveLeft"):
            self.agent_location = "B" if action == "MoveRight" else "A"

        self.performance += sum(1 for r in self.rooms.values() if r == "Clean")


def simple_reflex_agent(loc, rooms):
    if rooms[loc] == "Dirty":
        return "Suck"
    if rooms["A"] == rooms["B"] == "Clean":
        return "NoOp"
    return "MoveRight" if loc == "A" else "MoveLeft"


def run_simulation(loc, A, B, steps=10):
    env = VacuumEnvironment(loc, A, B)
    print(f"\nInitial: Loc={loc}, A={A}, B={B}")

    for step in range(steps):
        action = simple_reflex_agent(env.agent_location, env.rooms)
        print(f"Step {step+1}: Loc={env.agent_location}, "
              f"A={env.rooms['A']}, B={env.rooms['B']}, Action={action}")

        if action == "NoOp":
            break

        env.update(action)

    print("Performance:", env.performance)
    return env.performance


# Test all cases
for loc, A, B in itertools.product(["A", "B"], ["Clean", "Dirty"], ["Clean", "Dirty"]):
    run_simulation(loc, A, B)
