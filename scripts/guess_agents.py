from autogen import AssistantAgent,ConversableAgent
import random


model_config= [
    {
        "model": "llama3.1",
        "api_type": "ollama",
        "stream": True,
        "max_tokens":2500,
        "temperature":.8,
    },
]




gambler = ConversableAgent(
    name="Gamble Master",
    human_input_mode="NEVER",
    system_message=""" 
    First I am going to picks a random number between min and max (inclusive). and tell you the range.

    You have up to 10 rounds to guess the correct number.
    I will tell you:
    "Higher" if your guess is too low.
    "Lower" if your guess is too high.
    "YOU GOT IT" if your guess is correct.

    The Money Rules:
    The game starts with me owing you $5.
    Every time you guess wrong, the amount that owes you is reduced by $1 (e.g. round 2 I owe you 4 dollars, round 6 you owe me 1 dollar).

    If you guess the number within the 5 first rounds
    You get whatever money is currently owed to you
    Or, you owe me if you are still guessing after round 5
    The game ends when:
    You guess correctly or after 10 rounds without a correct guess — you owe me $5.
    Tell the player gAME FINISHED.

    """,
    llm_config={"config_list": model_config},
    #is_termination_msg=lambda msg: "TERMINATE" in msg["content"].upper(),

)

player = ConversableAgent(
    name="player",
    system_message="you are a player playing to win! Stay focused and avoid any gibberish talks.",
    llm_config={"config_list": model_config},
    human_input_mode="NEVER",
    #is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],

)






