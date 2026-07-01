from my_agent.agent import Agent

print("🤖 OmniAgent v2")

agent = Agent()

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    response = agent.run(user)

    print(f"\n🤖 {response}")