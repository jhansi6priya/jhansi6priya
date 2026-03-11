from datetime import datetime

content = f"""
#Automated README

Last updated: {datetime.now()}

Keep learning something new everyday
"""

with open("README.md", "w") as f:
    f.write(content)