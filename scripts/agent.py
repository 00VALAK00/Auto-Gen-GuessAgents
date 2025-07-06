from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor
from config.prompts import PromptTemplates
from pathlib import Path

# Setting up the code executor
workdir = Path("coding")
workdir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=workdir)


model_config= [
    {
        "model": "llama3.1",
        "api_type": "ollama"
    }
]

# configure the proxy agent responsible for executing what the assistant agent provides
proxy_agent= UserProxyAgent(
    name="proxy_agent",
    code_execution_config={"executor": code_executor},
    is_termination_msg=lambda msg: "FINISH" in msg.get("content"),
)


# configure the conversational agent

agent = AssistantAgent(
    name="ollama_agent",
    system_message=PromptTemplates.Ollama,
    llm_config={"config_list": model_config},
)



