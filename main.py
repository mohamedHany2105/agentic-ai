from ollama import chat
# from Tools.os_tools import tools_schema
import datetime
# print(tools_schema)
# print(datetime.datetime.now())

import subprocess
import os





def read_file(path='.'):
    data=""
    with open(path, encoding="utf-8") as f:
        data= f.read()
    return data

def write_file(path, content):
    print(path)
    data=""
    with open(path, "w",encoding="utf-8") as f:
        f.write(content)
    # return "write file done" or "failed to write file"

    return f"content saved at {path} at length of characters{len(content)}"
def make_dir(directory):
    os.makedirs(directory, exist_ok=True)
    return "done"
def list_files(directory='.'):
    entries = []
    for x in os.scandir(directory):
        entries.append(x.name + ('/' if  x.is_dir() else x.name))
    return '\n'.join(sorted(entries)) or "empty directory"
def run_command(command):
    acceptance= input(f"Run {command}: Y/n : ")
    if acceptance.strip().lower() != "y":
        print("User refuse to use Shell")

    command=subprocess.run(command, shell=True,capture_output=True,text=True)
    output = (command.stdout + command.stderr).strip()
    return output or f"no output, exit code {command.stderr}"


tools = {
    "read_file":read_file,
    "write_file":write_file,
    "make_dir":make_dir,
    "list_files":list_files,
    "run_command":run_command
}

tool_schema=[
    {
        "type":"fucntion",
        "function":
            {
            "name":"read_file",
            "description":"Tool to read files",
            "parameters":{
                    "type":"object",
                    "properties":{"path":{"type":"string"}},
                    "required":["path"]
            }
        },
    },
    {
        "type": "fucntion",
        "function":
            {
                "name": "write_file",
                "description": "create a new file or write in a specified file",
                "parameters": {
                    "type": "object",
                    "properties": {"path": {"type": "string"},"content": {"type": "string"}},
                    "required": ["path"]
                }
            },
    },
    {
        "type": "fucntion",
        "function":
            {
                "name": "make_dir",
                "description": "Make a new directory",
                "parameters": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"]
                }
            },
    },
    {
        "type":"fucntion",
        "function":
            {
            "name":"list_files",
            "description":"list files in the directory",
            "parameters":{
                    "type":"object",
                    "properties":{"path":{"type":"string"}},
                    "required":["path"]
            }
        },
    },
    {
        "type": "fucntion",
        "function":
            {
                "name": "run_command",
                "description": "Execute Command",
                "parameters": {
                    "type": "object",
                    "properties": {"command": {"type": "string"}},
                    "required": ["command"]
                }
            },
    }
]


# def run_agent():
#     while True:
#         user_input=input("YOU : ")
#         if user_input.strip().lower() ==["bye","exit","quit"]:
#             break
#         messages = [{
#             "role": "system",
#             "content": "Your name is :TOT , you have a access to Crud on directory as a assistant"
#         }, {
#             "role": "user",
#             "content": user_input
#         }
#         ]
#         agent = chat(messages=messages,model="qwen3.5:9b",tools=tool_schema, )
#
#
#         msg = agent["message"]
#         messages.append(msg)
#
#         if not msg.get("tool_calls"):
#             return msg["content"]  # final answer
#         for call in msg["tool_calls"]:
#             fn_name = call["function"]["name"]
#             args = call["function"]["arguments"]
#             result = tools[fn_name](**args)
#             messages.append({
#                 "role": "tool",
#                 "content": str(result),
#             })
#         # write the content in file
#
#
#
#         messages.append({"role":"user","content":agent})
#         print("BOT : " + agent.message.content)
#
def run_agent():
    messages = [{
        "role": "system",
        "content": "Your name is TOT, you have access to CRUD on directory as an assistant"
    }]

    while True:
        user_input = input("YOU : ")
        if user_input.strip().lower() in ["bye", "exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        agent = chat(messages=messages, model="qwen3.5:9b", tools=tool_schema)
        msg = agent["message"]
        messages.append(msg)

        if msg.get("tool_calls"):
            for call in msg["tool_calls"]:
                fn_name = call["function"]["name"]
                print(fn_name)
                args = call["function"]["arguments"]
                print(args)
                result = tools[fn_name](**args)
                print(call.get("tool_call_id"))
                messages.append({
                    "role": "tool",
                    "tool_call_id": call.get("id"),
                    "name": fn_name,
                    "content": str(result),
                })

            # ask the model again, now with tool results in context
            agent = chat(messages=messages, model="qwen3.5:9b", tools=tool_schema)
            msg = agent["message"]
            messages.append(msg)

        print("BOT : " + msg["content"])

#  can you make file called "fgggf" and write in it "wow this is the begin of agentic ai and im so happy to do that and i want to tell to myself i can do what i want , you are on the write way work hard and keep going ⚙️"


run_agent()
