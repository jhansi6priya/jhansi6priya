from datetime import datetime

content = f"""
# Hi, I'm Jhansi 👋

🚀 4th Year BTech Student  
💻 Learning Python, React, Cloud & DevOps  

### ⏳ Last Updated
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Keep building and learning every day ✨
"""

with open("README.md", "w") as f:
    f.write(content)
