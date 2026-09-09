import subprocess
import os





def read_file(path='.'):
    with open(path, encoding="utf-8") as f:
        return f.read()
def write_file(path, content):
    print(path)
    with open(path, "w",encoding="utf-8") as f:
        f.write(content)
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

tools_schema=[
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