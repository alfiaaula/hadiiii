import re

css_update = """
@media (max-width: 400px) {
    .doily-container {
        width: 250px;
        height: 330px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_update)
