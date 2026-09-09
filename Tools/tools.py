from os_tools import *




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
                "description": "Tool to read files",
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