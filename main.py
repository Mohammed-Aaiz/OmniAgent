from my_agent.brain import ask_ai
from my_agent.tool_manager import use_tool

print("🤖 OmniAgent v2")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    tool_result = use_tool(user)

    if tool_result is not None:
        print("\n🛠 Calculator:", tool_result)
        continue

    reply = ask_ai(user)

    print("\n🤖", reply)