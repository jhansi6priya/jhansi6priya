from datetime import datetime
import re

with open("README.md", "r") as f:
    readme = f.read()

new_Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_Sec = f"""
<!--LAST_UPDATED_START-->
{new_Date}
<!--LAST_UPDATED_END-->
"""

updated_readme = re.sub(
    r"<!--LAST_UPDATED_START-->.*?<!--LAST_UPDATED_END-->",
    new_Sec,
    readme,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(updated_readme)
