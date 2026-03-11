from datetime import datetime

content = f"""
### ⏳ Last Updated
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Keep building and learning every day ✨
"""

with open("README.md", "w") as f:
    f.write(content)
