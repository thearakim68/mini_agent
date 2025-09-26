import os 
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load OpenAI key
load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

# Add memory to the agent
memory = ConversationBufferMemory()

# Build conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Start the conversation loop
print("Start chatting with the agent. Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the chat. Goodbye!")
        break
    response = conversation.run(user_input)
    print(f"Agent: {response}")