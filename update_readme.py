from datetime import datetime

with open("README.md", "r") as f:
    readme = f.read()

new_Date = {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

content = readme.replace(f"
### ⏳ Last Updated
{new_Date}
Keep building and learning every day ✨
")

with open("README.md", "w") as f:
    f.write(content)
