import re

html_update = """
        <!-- Section 5: Menu 3 Objects -->
        <section id="sec-menu" class="section flex-center hidden">
            <div class="presentation-wrapper" style="container-type: inline-size;">
                <div class="menu-slide" style="position: relative; width: 100%; aspect-ratio: 16/9; background: #8c1c1c; border-radius: 1.5cqw; display: flex; justify-content: center; align-items: center; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                    
                    <!-- Stars Background -->
                    <div class="stars-bg"></div>

                    <!-- Lace Rectangular Mat -->
                    <div class="lace-rect">
                        <!-- Floral borders in the corners using SVGs (simplified elegant corners) -->
                        <div class="lace-corner top-left"></div>
                        <div class="lace-corner top-right"></div>
                        <div class="lace-corner bottom-left"></div>
                        <div class="lace-corner bottom-right"></div>

                        <!-- Inner Cream Oval -->
                        <div class="cream-oval-menu">
                            <h2 class="script-font menu-title-script" style="color: #4a1515; font-size: 5cqw; margin-bottom: 2cqw; margin-top: 1cqw;">For You...</h2>
                            <p class="handwriting-font" style="font-size: 2cqw; color: #4a1515; margin-bottom: 2cqw;">sedikit kejutan buat kamu, pilih salah satu ya</p>
                            
                            <!-- Red Pills Menu -->
                            <div class="pill-menu-grid">
                                <button class="pill-btn handwriting-font" onclick="openSubmenu('sec-music')">Our Song</button>
                                <button class="pill-btn handwriting-font" onclick="openSubmenu('sec-wishes')">Wishes</button>
                                <button class="pill-btn handwriting-font" onclick="openSubmenu('sec-gallery')" style="grid-column: span 2;">Memories</button>
                            </div>
                        </div>
                    </div>

                    <!-- Decorative Feather Quill SVG -->
                    <div class="feather-quill">
                        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
                            <defs>
                                <linearGradient id="featherGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" stop-color="#4a4a4a"/>
                                    <stop offset="50%" stop-color="#2a2a2a"/>
                                    <stop offset="100%" stop-color="#cfcfcf"/>
                                </linearGradient>
                            </defs>
                            <path d="M 85,15 C 80,10 65,15 50,30 C 40,40 30,55 25,65 C 20,75 15,85 10,90 C 8,92 5,90 10,85 C 20,75 30,60 40,50 C 50,40 65,30 80,25 C 85,25 90,20 85,15 Z" fill="url(#featherGrad)" opacity="0.9"/>
                            <path d="M 85,15 C 80,20 70,30 60,40 C 50,50 40,65 35,75 C 30,85 25,95 20,100 C 18,102 15,100 20,95 C 30,85 45,70 55,60 C 65,50 78,40 85,35 C 90,30 90,20 85,15 Z" fill="url(#featherGrad)" opacity="0.9"/>
                            <path d="M 12,98 L 90,10" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
                            <path d="M 25,75 C 20,70 15,68 18,72 M 35,65 C 30,60 25,58 28,62 M 45,55 C 40,50 35,48 38,52 M 65,35 C 60,30 55,28 58,32" stroke="#fcf8f2" stroke-width="1" fill="none" opacity="0.6"/>
                        </svg>
                    </div>

                </div>
            </div>
            
            <div class="flex flex-row justify-center mt-6 z-10 relative px-4" style="width: 100%; max-width: 900px;">
                <button class="btn-outline w-full bg-white opacity-90" onclick="navigateTo('sec-journey')">Kembali</button>
                <button class="btn-primary w-full opacity-90" onclick="navigateTo('sec-calendar')">Continue to Calendar</button>
            </div>
        </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<!-- Section 5: Menu 3 Objects -->.*?<\/section>', re.DOTALL)
text = pattern.sub(html_update, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
