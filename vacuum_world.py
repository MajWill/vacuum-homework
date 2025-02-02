from agents import *

loc_A, loc_B = 0, 1
class TrivialVacuumEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self):
        super().__init__()
        self.status = {
            loc_A: "Clean",
            loc_B: "Clean"
        }
        

    def thing_classes(self):
        return [
            Wall,
            Dirt,
            ReflexVacuumAgent,
        ]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""

        if action == "Right":
            agent.location = loc_B
            agent.performance -= 1
        elif action == "Left":
            agent.location = loc_A
            agent.performance -= 1
        elif action == "Suck":
            if self.status[agent.location] == "Dirty":
                agent.performance += 10
            self.status[agent.location] = "Clean"

    def performance_score(self, i, j, agent, action):

        self.status = [loc_A[i], loc_B[j]]

        self.execute_action(agent, action)
        print(agent.performance)

# Initialize the two-state environment
trivial_vacuum_env = TrivialVacuumEnvironment()


"""We change the simpleReflexAgentProgram so that it doesn't make use of the Rule class"""
def SimpleReflexAgentProgram():
    """This agent takes action based solely on the percept. [Figure 2.10]"""
    
    def program(percept):
        loc, status = percept
        return ('Suck' if status == 'Dirty' 
                else'Right' if loc == loc_A 
                            else'Left')
    return program

        
# Create a simple reflex agent the two-state environment
program = SimpleReflexAgentProgram()
simple_reflex_agent = Agent(program)

trivial_vacuum_env.add_thing(simple_reflex_agent)
total_score=0
for p in range(2):
    if p == 0:
        simple_reflex_agent.location = loc_A
    elif p == 1:
        simple_reflex_agent.location = loc_B
    for i in range(2):
        if i == 0:
            trivial_vacuum_env.status[loc_A] = "Clean"
        elif i == 1:
            trivial_vacuum_env.status[loc_A] = "Dirty"
        for j in range(2):
            if j == 0:
                trivial_vacuum_env.status[loc_B] = "Clean"
            elif j == 1:
                trivial_vacuum_env.status[loc_B] = "Dirty"
            # Location of the agent 
            print(f"SimpleReflexVacuumAgent is located at {simple_reflex_agent.location}.\n")

            # Check the current state of the environment
            print(f"State of the Environment: {trivial_vacuum_env.status}.\\n")

            # Run the environment
            trivial_vacuum_env.step()

            # Performance score after one step
            print(f"The score of the agent is {simple_reflex_agent.performance}.\n")
            total_score+= simple_reflex_agent.performance

            # New location of the agent after one step
            print(f"SimpleReflexVacuumAgent is located at {simple_reflex_agent.location}.\n")

            # trivial_vacuum_env.delete_thing(simple_reflex_agent)

# Average score

print(f" The avarage score of the agent is: {total_score/8}.")

print( trivial_vacuum_env.status)