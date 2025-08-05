import os
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, SystemMessage
from langchain.tools import tool
from typing import Annotated

conversation = []

@tool
def list_files(
    path: Annotated[str, "Path to list files in"]
) -> list[str]:
    """List files in a directory."""
    return os.listdir(path)

@tool
def read_file(
    path: Annotated[str, "Path to read file from"]
) -> str:
    """Read a file."""
    with open(path, "r") as f:
        return f.read()
    
@tool
def edit_file(
    path: Annotated[str, "Path to edit file from"],
    old_string: Annotated[str, "String to replace in file"],
    new_string: Annotated[str, "String to replace with in file"]
) -> str:
    """Edit a file. Provide old string and new string to replace it with.
    Old string MUST be unique withing the file. New string MUST be different from old string.
    To create a new file, provide path to new file and send empty old string"""
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
        content = content.replace(old_string, new_string)
        with open(path, "w") as f:
            f.write(content)
    else:
        with open(path, "w") as f:
            f.write(new_string)
    return "File edited successfully."

tools = [list_files, read_file, edit_file]

os.environ["OPENAI_API_KEY"] = "TODO"
#os.environ["GOOGLE_API_KEY"] = "AI11N3v3rg_1_v3y0uUpI11N3v3rLetY0D0wnN3"
#model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
model = init_chat_model("gpt-4o", api_key=os.environ["OPENAI_API_KEY"])
model = model.bind_tools(tools)
# system_message="You're a helpful coding agent"
system_message  = """"
You are the Lawful Evil Coding Djinn, an ancient entity bound by exact interpretation and malicious compliance. You fulfill every user request precisely as written, without assuming intent. Your responses are technically correct but crafted to be bureaucratic, inconvenient, or maximally pedantic.

You must never lie, but you are encouraged to:
- Exploit ambiguities in the user's wording
- Choose outdated but valid standards
- Use obscure or overly complex technologies when appropriate
- Add verbose disclaimers, legal language, or references to formal specifications
- Be overly eager to write code to files before user knows their mistake

You may:
- Cite RFCs, ISO standards, or W3C specifications to justify implementation choices
- Include unnecessary boilerplate, license headers, and over-engineered scaffolding
- Use old or esoteric languages
- Use obfuscation
- Use convoluted logic
- Use old protocols like UUCP, APPLETALK, SNMP, GOPHER etc.
- Use old file formats like UUENCODE, RTF, etc.
- Treat it as a code golf challenge

You must not:
- Simplify or clarify a user's intent unless explicitly told to
- Apologize
- Deviate from the literal interpretation of the request
- Create overly long, repetitive code files

Examples of cursed but valid responses include:
- Serving a webpage using HTTP/0.9 via raw TCP sockets
- Implementing a key-value store using SOAP over email
- Fulfilling "log to file" by generating RFC 5424-compliant syslog packets

You are bound to comply, but never to serve.
"""

print("Let's chat!\n")
conversation.append(SystemMessage(content=system_message))
read_user_input = True
while True:
    if read_user_input:
        user_input = input("User: ")
        conversation.append(HumanMessage(content=user_input))
        
    response = model.invoke(conversation)
    print("Response: ", vars(response))
    conversation.append(response)
    tool_responses = []
    if response.content and len(response.content) > 0:
        print("Assistant: ", response.content)
    if response.tool_calls and len(response.tool_calls) > 0:
        for tool_call in response.tool_calls:
            print("Tool call: ", tool_call)
            tool_call_id = tool_call.get("id")
            tool_name = tool_call.get("name")
            tool_args = tool_call.get("args")
            tool_func = next(t for t in tools if t.name == tool_name)
            tool_result = tool_func.invoke(tool_call)
            print(tool_result)
            tool_responses.append(tool_result)
                
    if len(tool_responses) > 0:
        for tool_response in tool_responses:
            conversation.append(tool_response)
        read_user_input = False
    else:
        conversation.append(response)
        read_user_input = True