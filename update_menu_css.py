css_append = """
/* Menu Design (sec-menu) Styles */
.lace-rect {
    width: 85%;
    height: 80%;
    background: #fff;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    border-radius: 1cqw;
    z-index: 2;
}

.lace-rect::before {
    content: '';
    position: absolute;
    inset: -1.5%;
    border-radius: 2cqw;
    border: 1.2cqw dotted #fff;
}

.lace-rect::after {
    content: '';
    position: absolute;
    inset: -3.5%;
    border-radius: 2.5cqw;
    border: 1cqw dotted rgba(255, 255, 255, 0.8);
}

.cream-oval-menu {
    width: 90%;
    height: 85%;
    background: #fcf8f2;
    border-radius: 50%;
    border: 0.3cqw dashed #b79f9f;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 5;
    padding: 2cqw;
    position: relative;
}

.menu-title-script {
    font-weight: normal;
    text-shadow: 0.2cqw 0.2cqw 0px rgba(0,0,0,0.1);
}

.pill-menu-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5cqw 2cqw;
    width: 80%;
    margin-top: 1cqw;
    justify-items: center;
}

.pill-btn {
    background: #ab1f1f;
    color: #fff;
    border: none;
    border-radius: 3cqw;
    padding: 1.2cqw 3cqw;
    font-size: 2.2cqw;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    width: 100%;
    transition: transform 0.2s, background 0.2s;
    text-align: center;
    letter-spacing: 0.1cqw;
}

.pill-btn:hover {
    transform: scale(1.05);
    background: #8c1c1c;
}

.feather-quill {
    position: absolute;
    bottom: -5%;
    right: -2%;
    width: 25cqw;
    height: auto;
    z-index: 10;
    filter: drop-shadow(0 10px 10px rgba(0,0,0,0.5));
    transform: rotate(10deg);
}

/* Optional corner lace decor approximation */
.lace-corner {
    position: absolute;
    width: 8cqw;
    height: 8cqw;
    background: radial-gradient(circle at center, transparent 40%, #fff 40%, #fff 60%, transparent 60%),
                radial-gradient(circle at center, transparent 40%, rgba(255,255,255,0.7) 40%, rgba(255,255,255,0.7) 70%, transparent 70%);
    background-size: 2cqw 2cqw, 1cqw 1cqw;
    border-radius: 50%;
    z-index: 3;
}
.lace-corner.top-left { top: -2cqw; left: -2cqw; }
.lace-corner.top-right { top: -2cqw; right: -2cqw; }
.lace-corner.bottom-left { bottom: -2cqw; left: -2cqw; }
.lace-corner.bottom-right { bottom: -2cqw; right: -2cqw; }
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
