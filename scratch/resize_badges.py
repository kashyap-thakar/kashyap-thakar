import re

def replace_badge(m):
    badge = m.group(0)
    # Only add height="28" if it's not already there and if it's a tech stack badge
    # The tech stack badges are the ones with -000000?style=flat
    if 'height=' not in badge and '-000000?style=flat' in badge:
        return badge.replace('alt=', 'height="26" alt=')
    return badge

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<img src="https://img\.shields\.io/badge/[^>]+>', replace_badge, content)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

with open('preview.html', 'r', encoding='utf-8') as f:
    content2 = f.read()
new_content2 = re.sub(r'<img src="https://img\.shields\.io/badge/[^>]+>', replace_badge, content2)
with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(new_content2)
