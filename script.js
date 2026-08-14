// Data for Letter (Draft configuration)
const letterPages = [
    "Halowww <br><br>i hope watching you grow, hustle, and stay strong through everything has been one of the things i'm most proud of.",
    "i'm so, so proud of you. not just because of what you've achieved, but because of the effort behind it. the sleepless nights, the stress you don't always talk about, the way you keep pushing even when things feel unfair. i see all of it. i really do.",
    "people might underestimate you now they might not see your worth yet, but i've never doubted you for a second. i know the kind of man you're becoming. i know how far you're going to go. and one day, all the things they questioned about you... you're going to become someone great. not because of luck, but because of everything you're willing to fight through."
];
let currentLetterPage = 0;

// Data for Gallery (Easily changeable later)
// File akan diambil dari folder fotokita/
const galleryFotos = [
    { src: 'fotokita/foto1.jpg', caption: 'Foto Pertama' },
    { src: 'fotokita/foto2.jpg', caption: 'Liburan bareng' },
    { src: 'fotokita/foto3.jpg', caption: 'Silly faces' },
    { src: 'fotokita/foto4.jpg', caption: 'Makan malam kesukaan' },
    { src: 'fotokita/foto5.jpg', caption: 'Candid moment' },
    { src: 'fotokita/foto6.jpg', caption: 'Our best sunset' },
    { src: '', caption: 'Untuk tahun 2027...', emptyAlbum: true }
];

// Data for Playlist (Easily changeable later)
// Ganti title, artist, img (bisa pakai foto kalian), dan src (file lagu di assets/) sesuka hati
const playlistSongs = [
    { title: 'Ramai sepi bersama', artist: 'Hindia', img: 'assets/vinyl.svg', src: 'assets/ramai_sepi_bersama.mp3' },
    { title: '1000x', artist: 'Ghea', img: 'assets/vinyl.svg', src: 'assets/1000x.mp3' },
    { title: 'Berhasil', artist: 'Perunggu', img: 'assets/vinyl.svg', src: 'assets/berhasil.mp3' },
    { title: 'Kita buat menyenangkan', artist: 'Bernadya', img: 'assets/vinyl.svg', src: 'assets/kita_buat_menyenangkan.mp3' }
];

// Data for Calendar Section (Easily changeable later)
// monthIndex: 0 = Januari ... 11 = Desember
const calendarData = {
    monthName: 'August',
    monthIndex: 7,
    year: 2026,
    day: 15,
    subtitle: 'My favorite person was born',
    message: "One year down; the rest of our lives to go. Happy birthday! You're my favorite, and I'm so grateful I've gotten to share this past year with you."
};

document.addEventListener('DOMContentLoaded', () => {
    initLetter();
    initGallery();
    initPlaylist();
    initCalendar();
});

// --- Calendar ---
function initCalendar() {
    const gridEl = document.getElementById('cal-grid');
    if (!gridEl) return;

    document.getElementById('cal-month').textContent = calendarData.monthName;
    document.getElementById('cal-year').textContent = calendarData.year;
    document.getElementById('cal-subtitle').textContent = calendarData.subtitle;
    document.getElementById('cal-message').textContent = calendarData.message;

    const firstDayOfWeek = new Date(calendarData.year, calendarData.monthIndex, 1).getDay(); // 0 = Sun
    const totalDays = new Date(calendarData.year, calendarData.monthIndex + 1, 0).getDate();
    const heartIcon = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-6.7-4.3-9.3-8.1C1 10.1 1.6 6.6 4.6 5.1c2.1-1 4.4-.3 5.9 1.4l1.5 1.7 1.5-1.7c1.5-1.7 3.8-2.4 5.9-1.4 3 1.5 3.6 5 1.9 7.8C18.7 16.7 12 21 12 21z"/></svg>';

    let html = '';
    for (let i = 0; i < firstDayOfWeek; i++) {
        html += '<span class="cal-cell cal-empty">0</span>';
    }
    for (let d = 1; d <= totalDays; d++) {
        const weekday = (firstDayOfWeek + d - 1) % 7;
        const isSunday = weekday === 0;
        const isSpecial = d === calendarData.day;
        let classes = 'cal-cell';
        if (isSunday) classes += ' cal-sunday';
        if (isSpecial) classes += ' cal-heart';
        html += `<span class="${classes}">${isSpecial ? heartIcon : d}</span>`;
    }
    gridEl.innerHTML = html;
}

// --- Navigation ---
function navigateTo(sectionId) {
    // Hide active sections
    document.querySelectorAll('.section.active').forEach(sec => {
        if (sec.id !== sectionId) {
            sec.classList.remove('active');
            setTimeout(() => {
                if (!sec.classList.contains('active')) {
                    sec.classList.add('hidden');
                }
            }, 600); // match css transition duration
        }
    });

    // Show target section
    const target = document.getElementById(sectionId);
    target.classList.remove('hidden');
    // Force reflow to allow transition
    void target.offsetWidth;
    target.classList.add('active');
}

// Special Submenu Nav (Returns to menu when closed)
let previousSection = 'sec-menu';
function openSubmenu(sectionId) {
    navigateTo(sectionId);
}
function closeSubmenu() {
    navigateTo(previousSection);
}

// --- Envelope Animation ---
function openEnvelope() {
    const envelope = document.getElementById('envelope');
    const btnContainer = document.getElementById('btn-envelope-container');

    if (envelope.classList.contains('open')) return;

    envelope.classList.add('open');
    if (btnContainer) {
        btnContainer.style.opacity = '0';
        btnContainer.style.pointerEvents = 'none';
    }

    setTimeout(() => {
        navigateTo('sec-letter');
    }, 1500);
}

function resetEnvelope() {
    const envelope = document.getElementById('envelope');
    const btnContainer = document.getElementById('btn-envelope-container');

    envelope.classList.remove('open');
    if (btnContainer) {
        btnContainer.style.opacity = '1';
        btnContainer.style.pointerEvents = 'auto';
    }
}

// --- Letter Pagination ---
function initLetter() {
    updateLetter();
    document.querySelector('.letter-next').addEventListener('click', () => {
        if (currentLetterPage < letterPages.length - 1) {
            currentLetterPage++;
            updateLetter();
        } else {
            // End of letter, proceed to Next section (Journey)
            navigateTo('sec-journey');
        }
    });

    document.querySelector('.letter-back').addEventListener('click', () => {
        if (currentLetterPage > 0) {
            currentLetterPage--;
            updateLetter();
        } else {
            // First page, clicking back goes to envelope and resets its state
            resetEnvelope();
            navigateTo('sec-envelope');
        }
    });
}

function updateLetter() {
    const content = document.getElementById('letter-content');
    const backBtn = document.querySelector('.letter-back');
    const nextBtn = document.querySelector('.letter-next');

    // Fade out text first for smooth transition
    content.style.opacity = 0;

    setTimeout(() => {
        content.innerHTML = letterPages[currentLetterPage];
        content.style.opacity = 1;
        content.style.transition = 'opacity 0.3s ease';

        // Update Buttons
        if (currentLetterPage === 0) {
            backBtn.textContent = 'Kembali';
            backBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        } else {
            backBtn.textContent = 'Back';
            backBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }

        if (currentLetterPage === letterPages.length - 1) {
            nextBtn.textContent = 'Read More';
        } else {
            nextBtn.textContent = 'Next';
        }
    }, 200);
}

// --- Playlist ---
const fallbackSongImg = `data:image/svg+xml;utf8,<svg fill="%23ddd" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="%23efe9e1"/><text x="50" y="50" font-family="sans-serif" font-size="10" text-anchor="middle" alignment-baseline="middle" fill="%23aa9e8f">Foto</text></svg>`;

let currentSongAudio = null;
let currentSongIndex = null;
let songProgressInterval = null;

function initPlaylist() {
    const grid = document.getElementById('playlist-grid');
    if (!grid) return;

    playlistSongs.forEach((song, i) => {
        const card = document.createElement('div');
        card.className = 'song-card';
        card.id = `song-card-${i}`;

        card.innerHTML = `
            <div class="song-photo-wrap">
                <img src="${song.img}" alt="${song.title}">
            </div>
            <div class="song-title serif-font">${song.title}<br><span style="font-size:0.8em; opacity:0.8">${song.artist}</span></div>
            <div class="song-progress">
                <div class="song-progress-fill" id="song-progress-fill-${i}"></div>
                <div class="song-progress-dot" id="song-progress-dot-${i}"></div>
            </div>
            <div class="song-controls">
                <button class="song-control-btn" data-action="back" aria-label="Rewind"><i data-lucide="rewind"></i></button>
                <button class="song-control-btn" data-action="toggle" id="song-toggle-${i}" aria-label="Play"><i data-lucide="play" id="song-icon-${i}"></i></button>
                <button class="song-control-btn" data-action="forward" aria-label="Forward"><i data-lucide="fast-forward"></i></button>
            </div>
        `;

        const img = card.querySelector('img');
        img.onerror = () => { img.src = fallbackSongImg; };

        card.querySelector(`#song-toggle-${i}`).addEventListener('click', () => toggleSong(i));

        grid.appendChild(card);
    });

    if (window.lucide) lucide.createIcons();
}

function toggleSong(i) {
    // If another song is playing, stop it first
    if (currentSongIndex !== null && currentSongIndex !== i) {
        stopSong(currentSongIndex);
    }

    const isThisPlaying = currentSongIndex === i;

    if (isThisPlaying) {
        stopSong(i);
        return;
    }

    const song = playlistSongs[i];
    currentSongAudio = new Audio(song.src);
    currentSongAudio.loop = true;
    currentSongAudio.play().catch(e => console.log('Audio error:', e));
    currentSongIndex = i;

    document.getElementById(`song-card-${i}`).classList.add('playing');
    document.getElementById(`song-icon-${i}`).setAttribute('data-lucide', 'pause');
    if (window.lucide) lucide.createIcons();

    let simulatedProgress = 0;
    songProgressInterval = setInterval(() => {
        simulatedProgress += 1;
        if (simulatedProgress > 100) simulatedProgress = 0;
        const fill = document.getElementById(`song-progress-fill-${i}`);
        const dot = document.getElementById(`song-progress-dot-${i}`);
        if (fill) fill.style.width = simulatedProgress + '%';
        if (dot) dot.style.left = simulatedProgress + '%';
    }, 300);
}

function stopSong(i) {
    if (currentSongAudio) {
        currentSongAudio.pause();
        currentSongAudio = null;
    }
    clearInterval(songProgressInterval);

    const card = document.getElementById(`song-card-${i}`);
    if (card) card.classList.remove('playing');
    const icon = document.getElementById(`song-icon-${i}`);
    if (icon) icon.setAttribute('data-lucide', 'play');
    if (window.lucide) lucide.createIcons();

    currentSongIndex = null;
}

// --- Gallery & Lightbox ---
function initGallery() {
    const container = document.getElementById('gallery-container');

    // Placeholder image base64 just in case "fotokita/" is empty
    const fallbackImage = `data:image/svg+xml;utf8,<svg fill="%23ddd" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="%23efe9e1"/><text x="50" y="50" font-family="sans-serif" font-size="10" text-anchor="middle" alignment-baseline="middle" fill="%23aa9e8f">Foto Belum Tersedia</text></svg>`;

    galleryFotos.forEach((foto, i) => {
        const polaroid = document.createElement('div');
        // Randomly pick frame style 
        const frameClass = Math.random() > 0.5 ? 'frame-red' : 'frame-plaid';
        // Add random rotation slightly
        const rotationStr = `rotate(${Math.random() * 6 - 3}deg)`;
        polaroid.className = `polaroid gallery-item ${frameClass}`;
        polaroid.style.transform = rotationStr;

        const img = document.createElement('img');
        img.src = foto.src;
        // On error, show fallback
        img.onerror = () => { img.src = fallbackImage; };

        const washitape = document.createElement('div');
        washitape.className = 'washi-tape';
        washitape.style.transform = `rotate(${Math.random() * 8 - 4}deg)`;
        washitape.style.top = '-10px';

        const caption = document.createElement('p');
        caption.className = 'handwriting-font text-center mt-2 font-bold';
        caption.textContent = foto.caption;

        polaroid.style.position = 'relative';
        if (foto.emptyAlbum) {
            polaroid.classList.add('empty-album');
            const scallopTop = document.createElement('div');
            scallopTop.className = 'scallop-top';
            const scallopBottom = document.createElement('div');
            scallopBottom.className = 'scallop-bottom';
            polaroid.appendChild(scallopTop);
            polaroid.appendChild(scallopBottom);

            const seal = document.createElement('div');
            seal.className = 'wax-seal wax-seal-red';
            seal.style.transform = 'scale(0.5)';
            seal.style.top = '5px';
            seal.style.left = '5px';
            seal.innerHTML = '<i data-lucide="heart" class="seal-icon"></i>';
            polaroid.appendChild(seal);

            const lace = document.createElement('div');
            lace.className = 'lace-corner bottom-right';
            lace.style.opacity = '0.5';
            polaroid.appendChild(lace);

            img.style.opacity = '0.2';
            img.style.filter = 'sepia(1)';
        }

        polaroid.appendChild(washitape);
        polaroid.appendChild(img);
        polaroid.appendChild(caption);

        polaroid.addEventListener('click', () => openLightbox(img.src, foto.caption));

        container.appendChild(polaroid);
    });
}

function openLightbox(src, captionText) {
    const lightbox = document.getElementById('lightbox');
    const img = document.getElementById('lightbox-img');
    const caption = document.getElementById('lightbox-caption');

    img.src = src;
    caption.textContent = captionText;

    lightbox.classList.remove('hidden');
    // small timeout to allow layout before transition
    setTimeout(() => {
        lightbox.classList.add('active');
    }, 10);
}

function closeLightbox(e) {
    if (e.target.tagName !== 'IMG') {
        const lightbox = document.getElementById('lightbox');
        lightbox.classList.remove('active');
        setTimeout(() => lightbox.classList.add('hidden'), 300);
    }
}
