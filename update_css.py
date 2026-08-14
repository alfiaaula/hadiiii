
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Presentation Slide Styles */
.presentation-wrapper {
    width: 100%;
    max-width: 900px;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    container-type: inline-size;
}

.presentation-slide {
    display: flex;
    flex-direction: row;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #fcf8f2;
    border-radius: 1.5cqw;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    overflow: hidden;
    position: relative;
}

/* Force Landscape layout always */
.slide-left {
    flex: 1;
    background-color: #8c1c1c;
    background-image: repeating-linear-gradient(
        90deg,
        #8c1c1c 0%,
        #8c1c1c 5%,
        #6d1414 5%,
        #6d1414 10%
    );
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 3cqw;
    overflow: hidden;
}

.stars-bg {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    background-image: url('data:image/svg+xml;utf8,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><g fill="%23ecd299"><path d="M10,0 L13,6 L20,7 L14,12 L16,19 L10,15 L4,19 L6,12 L0,7 L7,6 Z" transform="scale(0.5) translate(40, 40)"/><path d="M10,0 L13,6 L20,7 L14,12 L16,19 L10,15 L4,19 L6,12 L0,7 L7,6 Z" transform="scale(0.4) translate(150, 150) rotate(20)"/><path d="M10,0 L13,6 L20,7 L14,12 L16,19 L10,15 L4,19 L6,12 L0,7 L7,6 Z" transform="scale(0.6) translate(10, 100) rotate(-15)"/></g></svg>');
    opacity: 0.8;
}

/* Simulated Doily using dotted borders */
.doily-container {
    width: 80%;
    aspect-ratio: 3.5 / 4.5;
    background: #fff;
    border-radius: 50%;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    z-index: 2;
}

.doily-container::before {
    content: '';
    position: absolute;
    inset: -3%;
    border-radius: 50%;
    border: 1.5cqw dotted #fff;
}

.doily-container::after {
    content: '';
    position: absolute;
    inset: -6%;
    border-radius: 50%;
    border: 1.2cqw dotted rgba(255, 255, 255, 0.9);
}

.doily-inner {
    width: 86%;
    height: 86%;
    border-radius: 50%;
    border: 0.2cqw dashed #b79f9f;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #fcf8f2;
    z-index: 10;
    padding: 3cqw;
}

.doily-text-1 {
    font-size: 2cqw;
    color: #8c1c1c;
    margin-bottom: 0.2cqw;
}

.doily-warning {
    font-size: 1.8cqw;
    color: #8c1c1c;
    text-align: center;
    margin-bottom: 0.5cqw;
    line-height: 1.2;
}

.doily-list {
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: left;
    color: #8c1c1c;
    font-size: 1.7cqw;
}

.doily-list li {
    position: relative;
    padding-left: 2cqw;
    line-height: 1.5;
}

.doily-list li::before {
    content: '•';
    position: absolute;
    left: 0;
    top: 0;
    color: #8c1c1c;
}

/* Watermark Badge */
.watermark-badge {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #000;
    color: #fff;
    font-family: sans-serif;
    font-size: 1.2cqw;
    padding: 0.5cqw 1.5cqw;
    border-radius: 2cqw;
    z-index: 20;
    letter-spacing: 0.05cqw;
    font-weight: bold;
    white-space: nowrap;
}

.slide-right {
    flex: 1.1;
    background-color: #fcf8f2;
    padding: 4cqw;
    display: flex;
    align-items: center;
    justify-content: center;
}

.months-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 3cqw;
    row-gap: 2cqw;
    width: 100%;
}

.month-item {
    font-size: 2.5cqw;
    color: #2b1212;
    position: relative;
    display: inline-block;
    padding: 0.2cqw 1cqw;
    letter-spacing: 0.1cqw;
    white-space: nowrap;
}

.circled-month {
    position: relative;
    z-index: 1;
}

.circle-svg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-45%, -50%);
    width: 130%;
    height: 170%;
    z-index: -1;
    pointer-events: none;
}

.circle-svg path {
    stroke: #4A1515;
    fill: none;
    stroke-width: 0.3cqw;
    stroke-linecap: round;
}
""")
