import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Define the old section 5
    old_sec_menu_pattern = r'<!-- Section 5: Menu 3 Objects -->.*?<!-- Section 6: Music Player \(Playlist\) -->'
    
    new_sec_menu = """<!-- Section 5: Menu 4 Objects -->
        <section id="sec-menu" class="section flex-center hidden">
            <div class="menu-container" style="width: 100%; max-width: 800px; padding: 20px;">
                <h3 class="script-font text-cream text-center mb-2" style="font-size: 4.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">For You...</h3>
                <p class="handwriting-font text-cream text-2xl text-center mb-10" style="opacity: 0.9;">Pilih kotak mana saja yang mau kamu buka</p>
                
                <div class="features-grid">
                    <!-- Memories -->
                    <div class="feature-square" onclick="openSubmenu('sec-gallery')">
                        <div class="washi-tape" style="top: -10px; right: -10px; transform: rotate(15deg);"></div>
                        <div class="feat-icon-wrapper">
                            <i data-lucide="image" class="feat-icon"></i>
                        </div>
                        <span class="feat-title serif-font">Memories</span>
                    </div>
                    
                    <!-- List Song -->
                    <div class="feature-square" onclick="openSubmenu('sec-music')">
                        <div class="deco-star" style="top: -10px; left: -10px; transform: scale(1.2);"></div>
                        <div class="feat-icon-wrapper">
                            <i data-lucide="music" class="feat-icon"></i>
                        </div>
                        <span class="feat-title serif-font">Our Song</span>
                    </div>
                    
                    <!-- Calendar -->
                    <div class="feature-square" onclick="openSubmenu('sec-calendar')">
                        <div class="deco-cherry" style="bottom: -20px; right: -20px; transform: scale(0.7);"></div>
                        <div class="feat-icon-wrapper">
                            <i data-lucide="calendar-heart" class="feat-icon"></i>
                        </div>
                        <span class="feat-title serif-font">Calendar</span>
                    </div>
                    
                    <!-- Wishes -->
                    <div class="feature-square" onclick="openSubmenu('sec-wishes')">
                        <div class="deco-flower" style="top: -20px; left: 50%; margin-left: -35px; transform: scale(0.7);"></div>
                        <div class="feat-icon-wrapper">
                            <i data-lucide="sparkles" class="feat-icon"></i>
                        </div>
                        <span class="feat-title serif-font">Wishes</span>
                    </div>
                </div>
                
                <div class="flex flex-row justify-center mt-10">
                    <button class="btn-outline" style="color: #F5EFE6; border-color: #F5EFE6; padding: 10px 30px; font-size: 1.1rem; background: rgba(0,0,0,0.1);" onclick="navigateTo('sec-journey')">Kembali</button>
                </div>
            </div>
        </section>

        <!-- Section 6: Music Player (Playlist) -->"""

    html = re.sub(old_sec_menu_pattern, new_sec_menu, html, flags=re.DOTALL)
    
    # Update Calendar back button to use closeSubmenu()
    calendar_btn_old = """<div class="flex flex-row justify-center gap-4 mt-8">
                <button class="btn-outline" onclick="navigateTo('sec-menu')">Kembali</button>
                <button class="btn-primary" onclick="navigateTo('sec-cover')">Back to Start</button>
            </div>"""
    calendar_btn_new = """<div class="flex flex-row justify-center gap-4 mt-8">
                <button class="btn-outline" onclick="closeSubmenu()">Kembali</button>
                <button class="btn-primary" onclick="navigateTo('sec-cover')">Back to Start</button>
            </div>"""
    html = html.replace(calendar_btn_old, calendar_btn_new)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def update_css():
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    new_css = """
/* Features Grid for sec-menu */
.features-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    width: 100%;
}

@media (max-width: 768px) {
    .features-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }
}

.feature-square {
    position: relative;
    aspect-ratio: 1 / 1;
    background: var(--color-cream);
    border-radius: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s;
    border: 3px solid var(--color-maroon-dark);
}

.feature-square:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3);
}

.feat-icon-wrapper {
    width: 70px;
    height: 70px;
    background: var(--color-maroon);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
    box-shadow: 0 4px 10px rgba(122, 31, 43, 0.3);
    transition: background 0.3s, transform 0.3s;
}

.feature-square:hover .feat-icon-wrapper {
    background: var(--color-gold);
    transform: rotate(5deg) scale(1.1);
}

.feat-icon {
    width: 32px;
    height: 32px;
    color: var(--color-cream);
}

.feature-square:hover .feat-icon {
    color: var(--color-maroon);
}

.feat-title {
    color: var(--color-maroon);
    font-size: 1.4rem;
    font-weight: bold;
    text-align: center;
}
"""
    if "/* Features Grid for sec-menu */" not in css:
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write(new_css)

if __name__ == "__main__":
    update_html()
    update_css()
    print("Updated successfully")
