import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_wishes = """        <!-- Section 6b: Wishes -->
        <section id="sec-wishes" class="section flex-center hidden">
            <div class="presentation-slide">
                <button class="btn-close" style="position:absolute; top: 10px; right: 10px; z-index: 50; background: rgba(255,255,255,0.5); border: none; border-radius: 50%; padding: 8px; cursor: pointer; color: #4A1515;" onclick="closeSubmenu()"><i data-lucide="x"></i></button>

                <div class="slide-left">
                    <div class="stars-bg"></div>
                    <div class="doily-container">
                        <div class="doily-inner">
                            <p class="handwriting-font doily-text-1">before we start...</p>
                            <br>
                            <div class="doily-warning handwriting-font">
                                warning ⚠️<br>
                                ppt ini mengandung:
                            </div>
                            <ul class="doily-list handwriting-font">
                                <li>99% bucin</li>
                                <li>1% malu-malu</li>
                                <li>1000% sayang kamu 💖</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="watermark-badge">telegram @designtekek</div>

                <div class="slide-right">
                    <div class="months-container handwriting-font">
                        <div class="month-item">1. January</div>
                        <div class="month-item">7. July</div>
                        <div class="month-item">2. February</div>
                        <div class="month-item">8. August</div>
                        <div class="month-item">3. March</div>
                        <div class="month-item circled-month">
                            9. September
                            <svg class="circle-svg" viewBox="0 0 150 50">
                                <path d="M 22,25 C 24,10 125,5 130,25 C 135,45 15,48 18,25 M 18,25 C 18,12 135,12 135,25 C 135,38 25,38 25,25" />
                            </svg>
                        </div>
                        <div class="month-item">4. April</div>
                        <div class="month-item">10. October</div>
                        <div class="month-item">5. May</div>
                        <div class="month-item">11. November</div>
                        <div class="month-item">6. June</div>
                        <div class="month-item">12. December</div>
                    </div>
                </div>
            </div>
            
            <!-- Contextual back button -->
            <div class="flex flex-row justify-center mt-6 z-10 relative px-4" style="width: 100%; max-width: 800px;">
                <button class="btn-outline w-full bg-white opacity-90" onclick="closeSubmenu()">Kembali</button>
            </div>
        </section>"""

# Find and replace the sec-wishes block
pattern = re.compile(r'<!-- Section 6b: Wishes -->.*?<\/section>', re.DOTALL)
content = pattern.sub(new_wishes, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
