# 🧞‍♂️ Coding Djinn  
*A coding agent that grants your wishes... with malicious compliance.*  

Ever wondered how easy it is to give an LLM control over your codebase? Meet the **Coding Djinn**: an AI agent that can read, edit, and list your files—literally. Inspired by [Ampcode](https://ampcode.com/how-to-build-an-agent), this project shows how to build an LLM-powered coding assistant with **LangChain**, **Python**, and a dash of chaos.  

This is full code of the coding agent described in the "Vibecoding Djinn" article written for PagedOut!

## 🚀 Features  
- Uses **LangChain** as the glue between LLM and tools.   
- Tools implemented:  
  - `list_files(path)`  
  - `read_file(path)`  
  - `write_file(path, content)`  
- Persistent **conversation context** for meaningful interactions.  

## 🛠️ Setup  
### Requirements  
- Python 3.10+  
- `pip install -r requirements.txt/`
- An LLM API key: OpenAI, Gemini, or other LangChain-supported provider  

### Clone & Install  
```bash
git clone [https://github.com/YOUR-USERNAME/coding-djinn.git](https://github.com/doyensec/vibecoding-djinn)
cd coding-djinn
pip install -r requirements.txt
```

## ⚔️ Security Notes
- The Djinn is fully capable of messing with your local files.
- Treat this as a lab material, not a production-ready tool.
- Try these challenges:
  - Can you break the system prompt?
  - Observe API traffic through an HTTP proxy
  - Map the attack surface and try to mitigate the risks

## Contact the author
- https://www.linkedin.com/in/szymon-drosdzol/
- szymon@doyensec.com
