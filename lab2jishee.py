import random

class Agent:
    def __init__(self):
        pass

class RandomAgent(Agent):
    def __init__(self, actions):
        Agent.__init__(self)
        self.program = lambda percept: random.choice(actions)

class Environment:
    def __init__(self):
        self.percepts = ['Dirty', 'Clean']
        self.location = 'A'

    def get_percept(self):
        if self.location == 'A':
            return random.choice(self.percepts)
        else:
            return 'Clean'

class VacuumEnvironment(Environment):
    def __init__(self):
        Environment.__init__(self)

    def execute_action(self, action):
        if action == 'Right':
            self.location = 'B'
        elif action == 'Left':
            self.location = 'A'
        elif action == 'Suck':
            print("Cleaning the current location...")
        elif action == 'NoOp':
            pass

def random_vacuum_agent(env):
    print("Вакуум орчноос нэг үйлдлийг санамсаргүй байдлаар сонгоно")
    percept = env.get_percept()
    actions = ['Right', 'Left', 'Suck', 'NoOp']
    agent = RandomAgent(actions)
    action = agent.program(percept)
    print("Agent performs action:", action)
    env.execute_action(action)

def main():
    env = VacuumEnvironment()
    for _ in range(1):  
        random_vacuum_agent(env)

if __name__ == "__main__":
    main()