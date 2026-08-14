import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the watermark from sec-wishes
html = html.replace('<div class="watermark-badge">telegram @designtekek</div>', '')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
