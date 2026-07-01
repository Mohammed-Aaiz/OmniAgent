from my_agent.brain import ask_ai
from my_agent.tool_manager import use_tool
from memory.memory import load_memory, save_memory


class Agent:

    def __init__(self):
        self.history = load_memory()

    def run(self, user):

        tool_result = use_tool(user)

        if tool_result is not None:
            response = str(tool_result)

        else:
            response = ask_ai(user)

        self.history.append({
            "user": user,
            "assistant": response
        })

        save_memory(self.history)

        return response