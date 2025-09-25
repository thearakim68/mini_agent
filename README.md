# 🧠 Mini Agent Loop – My First AI Assistant

This project is a small but meaningful step in my journey into Agentic AI.  
It simulates how a basic AI agent thinks through tasks using OpenAI's GPT-4 API.

---

## 🧩 What It Does

The script takes a few example tasks—like math, weather checks, and summaries—and sends each one to the language model.  
It’s a minimal setup, but it clearly shows how an agent processes tasks step-by-step:

- Accepts a task  
- Sends it to the model  
- Prints the AI’s response  

It follows the core cycle of agentic thinking:  
**input → reasoning → output**

---

## 🛠 How to Run It

1. Clone this repository and navigate into it:

   ```bash
   git clone https://github.com/yourusername/mini_agent.git
   cd mini_agent

2. Create a virtual environment:
    
    ```bash
    python3 -m venv agentic_env
    source agentic_env/bin/activate  # On Mac/Linux

3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt

4. Create .env file in the root folder and add your OpenAI API key:
    
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here

5. Run the agent:

    ```bash
    python hello_agent.py

## ✏️ Sample Output

1. Math Task:
- [Agent received task]: do math  
- [Agent output]: The result of 15 * 4 is 60.

2. Text Summary Task:
- [Agent received task]: summarize text  
- [Agent output]: The text discusses how AI is rapidly transforming the digital world by improving automation, personalization, and decision-making.

3. Weather Task:
- [Agent received task]: search weather  
- [Agent output]: I'm an AI model and don't have real-time weather data access. If you'd like, I can show how you'd use an API like OpenWeather to do that.


## ⚙️ Tech Stack

- Python 3.11+
- OpenAI GPT-4 API
- Dotenv


## 🙆 About Me
*Kim Theara
UX/UI Designer / Generative AI Enthusiast / AI Researcher 

- 🌐[theara-me.webflow.io](https://theara-me.webflow.io/)
- 🔗[LinkedIn](https://www.linkedin.com/in/kimtheara-productdesign-ai-expert/)
- 🧑‍💻[Medium](https://medium.com/@thearakim68)