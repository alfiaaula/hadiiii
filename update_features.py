import re

# 1. Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Update galleryFotos
gallery_old = """const galleryFotos = [
    { src: 'fotokita/foto1.jpg', caption: 'First Date' },
    { src: 'fotokita/foto2.jpg', caption: 'Liburan bareng' },
    { src: 'fotokita/foto3.jpg', caption: 'Silly faces' },
    { src: 'fotokita/foto4.jpg', caption: 'Makan malam kesukaan' },
    { src: 'fotokita/foto5.jpg', caption: 'Candid moment' },
    { src: 'fotokita/foto6.jpg', caption: 'Our best sunset' }
];"""
gallery_new = """const galleryFotos = [
    { src: 'fotokita/foto1.jpg', caption: 'First Date' },
    { src: 'fotokita/foto2.jpg', caption: 'Liburan bareng' },
    { src: 'fotokita/foto3.jpg', caption: 'Silly faces' },
    { src: 'fotokita/foto4.jpg', caption: 'Makan malam kesukaan' },
    { src: 'fotokita/foto5.jpg', caption: 'Candid moment' },
    { src: 'fotokita/foto6.jpg', caption: 'Our best sunset' },
    { src: '', caption: 'Untuk tahun 2027...', emptyAlbum: true }
];"""
content = content.replace(gallery_old, gallery_new)

# Update Playlist
playlist_old = """const playlistSongs = [
    { title: 'Perfect', artist: 'Ed Sheeran', img: 'fotokita/foto1.jpg', src: 'assets/song.mp3' },
    { title: 'Lagu 2', artist: 'Nama Artis', img: 'fotokita/foto2.jpg', src: 'assets/song.mp3' },
    { title: 'Lagu 3', artist: 'Nama Artis', img: 'fotokita/foto3.jpg', src: 'assets/song.mp3' },
    { title: 'Lagu 4', artist: 'Nama Artis', img: 'fotokita/foto4.jpg', src: 'assets/song.mp3' },
    { title: 'Lagu 5', artist: 'Nama Artis', img: 'fotokita/foto5.jpg', src: 'assets/song.mp3' },
    { title: 'Lagu 6', artist: 'Nama Artis', img: 'fotokita/foto6.jpg', src: 'assets/song.mp3' }
];"""
playlist_new = """const playlistSongs = [
    { title: 'Ramai sepi bersama', artist: 'Hindia', img: 'assets/vinyl.svg', src: 'assets/ramai_sepi_bersama.mp3' },
    { title: '1000x', artist: 'Ghea', img: 'assets/vinyl.svg', src: 'assets/1000x.mp3' },
    { title: 'Berhasil', artist: 'Perunggu', img: 'assets/vinyl.svg', src: 'assets/berhasil.mp3' },
    { title: 'Kita buat menyenangkan', artist: 'Bernadya', img: 'assets/vinyl.svg', src: 'assets/kita_buat_menyenangkan.mp3' }
];"""
content = content.replace(playlist_old, playlist_new)

# Update Calendar year
content = re.sub(r'year: 2023,', 'year: 2026,', content)

# Update initGallery to handle emptyAlbum
init_gallery_target = """        polaroid.style.position = 'relative';
        polaroid.appendChild(washitape);
        polaroid.appendChild(img);
        polaroid.appendChild(caption);"""

init_gallery_replace = """        polaroid.style.position = 'relative';
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
        polaroid.appendChild(caption);"""

content = content.replace(init_gallery_target, init_gallery_replace)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()

# Add spinning animation for vinyl records
spinning_css = """
.song-card.playing .song-photo-wrap {
    box-shadow: 0 0 0 2px var(--color-gold);
}"""
spinning_replace = """
.song-card.playing .song-photo-wrap {
    box-shadow: 0 0 0 2px var(--color-gold);
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
.song-photo-wrap img[src$="vinyl.svg"] {
    border-radius: 50%;
}
.song-card.playing .song-photo-wrap img[src$="vinyl.svg"] {
    animation: spin 3s linear infinite;
}
.song-photo-wrap {
    border-radius: 50%;
    background: transparent;
}
"""
style_content = style_content.replace(spinning_css, spinning_replace)

# Ensure grid spacing works nicely for 4 items
grid_css = """    grid-template-columns: repeat(3, 1fr);
    gap: 1.4rem 1.2rem;"""
grid_replace = """    grid-template-columns: repeat(2, 1fr);
    gap: 1.4rem 1.2rem;"""
style_content = style_content.replace(grid_css, grid_replace)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(style_content)

print("Updates completed successfully.")
