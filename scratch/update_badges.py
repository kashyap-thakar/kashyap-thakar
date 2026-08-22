import re

def replace_badge(m):
    badge = m.group(0)
    # Make background black
    badge = badge.replace('-ffffff?', '-000000?')
    badge = badge.replace('labelColor=ffffff', 'labelColor=000000')
    badge = badge.replace('color=ffffff', 'color=000000')
    
    # Fix dark logos by making them white
    badge = badge.replace('logoColor=000000', 'logoColor=white')
    badge = badge.replace('logoColor=181717', 'logoColor=white') # GitHub
    badge = badge.replace('logoColor=191919', 'logoColor=white') # Anthropic
    badge = badge.replace('logoColor=1D1D1D', 'logoColor=white') # Rive
    badge = badge.replace('logoColor=050038', 'logoColor=white') # Miro
    badge = badge.replace('logoColor=263238', 'logoColor=white') # Directus
    badge = badge.replace('logoColor=2D3748', 'logoColor=white') # Prisma
    badge = badge.replace('logoColor=0D0E12', 'logoColor=white') # Sanity
    badge = badge.replace('logoColor=362D59', 'logoColor=white') # Sentry
    return badge

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'https://img\.shields\.io/badge/[^\"]+', replace_badge, content)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

with open('preview.html', 'r', encoding='utf-8') as f:
    content2 = f.read()
new_content2 = re.sub(r'https://img\.shields\.io/badge/[^\"]+', replace_badge, content2)
with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(new_content2)
