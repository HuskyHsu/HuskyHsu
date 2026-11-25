"""Generate RotomDex-style SVG project cards for the GitHub profile README."""

import base64
import html
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ICON_DIR = ROOT_DIR / "assets" / "icons"
OUT_DIR = ROOT_DIR / "assets" / "cards"

CARDS = [
    # Hardware, Desktop & Creative Tools
    {
        "id": "ghost-pad",
        "title": "Ghost Pad",
        "subtitle": "PC → Switch Controller Bridge",
        "created": "2026-10",
        "stack": "Tauri · Rust · UART · ESP32",
        "status": "Active",
        "grad": ("#eef2ff", "#ecfeff"),
        "icon": "ghost-pad.svg",
        "mode": "contain",
    },
    {
        "id": "he-kim-koo",
        "title": "Hé Kim Koo",
        "subtitle": "Firefly · Garmin GPS Trail",
        "created": "2026-11",
        "stack": "Monkey C · Connect IQ · MapLibre",
        "status": "In Progress",
        "grad": ("#f0fdf4", "#fefce8"),
        "icon": "he-kim-koo.svg",
        "mode": "contain",
    },
    {
        "id": "dot-weaver",
        "title": "Dot Weaver",
        "subtitle": "Pixel & Perler Bead Studio",
        "created": "2026-05",
        "stack": "React · Infinite Canvas · PWA",
        "status": "Active",
        "grad": ("#fdf2f8", "#eef2ff"),
        "icon": "dot-weaver.png",
        "mode": "contain",
    },
    {
        "id": "somnus",
        "title": "Somnus",
        "subtitle": "4-7-8 Neuro-Acoustic Sleep",
        "created": "2026-06",
        "stack": "React · Web Audio API · PWA",
        "status": "Active",
        "grad": ("#eff6ff", "#eef2ff"),
        "icon": "somnus.png",
        "mode": "contain",
    },
    # Pokédex & Gaming
    {
        "id": "lumiose",
        "title": "Lumiose",
        "subtitle": "Legends Z-A Pokédex",
        "created": "2025-10",
        "stack": "React · Tailwind · PWA",
        "status": "Active",
        "grad": ("#e9faf5", "#f6fbed"),
        "icon": "lumiose.png",
        "mode": "bleed",
    },
    {
        "id": "paldea",
        "title": "Paldea",
        "subtitle": "Scarlet & Violet Pokédex",
        "created": "2022-11",
        "stack": "React · TanStack Query · Zustand",
        "status": "Active",
        "grad": ("#fceef3", "#fff9eb"),
        "icon": "paldea.png",
        "mode": "bleed",
    },
    {
        "id": "arceus",
        "title": "Hisui",
        "subtitle": "Legends Arceus Pokédex",
        "created": "2022-02",
        "stack": "React · Leaflet Map · Vite",
        "status": "Active",
        "grad": ("#fff4d6", "#fffbe8"),
        "icon": "arceus.png",
        "mode": "bleed",
    },
    {
        "id": "galar",
        "title": "Galar",
        "subtitle": "Sword & Shield Pokédex",
        "created": "2024-02",
        "stack": "React · TanStack Query · Zustand",
        "status": "Active",
        "grad": ("#ebf4ff", "#f6efff"),
        "icon": "galar.png",
        "mode": "bleed",
    },
    {
        "id": "kanto",
        "title": "Kanto",
        "subtitle": "FireRed & LeafGreen Pokédex",
        "created": "2026-03",
        "stack": "React · Tailwind · PWA",
        "status": "Active",
        "grad": ("#fff0f2", "#f2faee"),
        "icon": "kanto.png",
        "mode": "bleed",
    },
    {
        "id": "rotomdex",
        "title": "RotomDex",
        "subtitle": "Unified Multi-Gen Pokédex",
        "created": "2026-07",
        "stack": "Vanilla JS · Zero-Dep · PWA",
        "status": "Active",
        "grad": ("#fff1eb", "#ffe9e6"),
        "icon": "rotomdex.png",
        "mode": "contain",
    },
    {
        "id": "sleepoke",
        "title": "SleePoke",
        "subtitle": "Pokémon Sleep Companion",
        "created": "2023-07",
        "stack": "React · TypeScript · Tailwind",
        "status": "Discontinued",
        "grad": ("#eef2ff", "#f5f3ff"),
        "icon": "sleepoke.png",
        "mode": "contain",
    },
    {
        "id": "nooklink",
        "title": "NookLink",
        "subtitle": "Animal Crossing: New Horizons",
        "created": "2020-04",
        "stack": "Node.js · Bottender · LINE Bot",
        "status": "Discontinued",
        "grad": ("#ecfdf5", "#fefce8"),
        "icon": "nooklink_icon.png",
        "mode": "contain",
    },
]

FOCUS_CARDS = [
    {
        "id": "focus-backend",
        "title": "Backend Architecture",
        "desc": "High-concurrency services for networking & cloud",
        "meta": "Node.js · Go · Rust · System Design",
        "grad": ("#eef2ff", "#e0f2fe"),
        "badge_bg": "#e0e7ff",
        "accent": "#4f46e5",
        "icon_svg": (
            '<rect x="1.5" y="2" width="13" height="5" rx="1.5"/>'
            '<rect x="1.5" y="9" width="13" height="5" rx="1.5"/>'
            '<circle cx="4.5" cy="4.5" r="0.6" fill="#4f46e5"/>'
            '<circle cx="4.5" cy="11.5" r="0.6" fill="#4f46e5"/>'
        ),
    },
    {
        "id": "focus-realtime",
        "title": "Real-time Systems",
        "desc": "Bidirectional communication & distributed design",
        "meta": "gRPC · WebSocket · Event-Driven",
        "grad": ("#ecfdf5", "#ecfeff"),
        "badge_bg": "#ccfbf1",
        "accent": "#0d9488",
        "icon_svg": (
            '<path d="M2 5.5h12m0 0-3-3m3 3-3 3"/>'
            '<path d="M14 10.5H2m0 0 3-3m-3 3 3 3"/>'
        ),
    },
    {
        "id": "focus-data",
        "title": "Data & Caching Systems",
        "desc": "Relational, NoSQL & caching for high-throughput",
        "meta": "PostgreSQL · MySQL · Redis · DynamoDB",
        "grad": ("#fdf2f8", "#f5f3ff"),
        "badge_bg": "#ede9fe",
        "accent": "#7c3aed",
        "icon_svg": (
            '<ellipse cx="8" cy="3.5" rx="5.5" ry="2"/>'
            '<path d="M2.5 3.5v9c0 1.1 2.46 2 5.5 2s5.5-.9 5.5-2v-9"/>'
            '<path d="M2.5 8c0 1.1 2.46 2 5.5 2s5.5-.9 5.5-2"/>'
        ),
    },
    {
        "id": "focus-cloud",
        "title": "Cloud Infrastructure",
        "desc": "Scalable AWS cloud architecture & deployment",
        "meta": "AWS · Docker · Kubernetes",
        "grad": ("#fff7ed", "#fefce8"),
        "badge_bg": "#fef3c7",
        "accent": "#d97706",
        "icon_svg": (
            '<path d="M4.5 13h7.5a3 3 0 0 0 .4-5.97A4.5 4.5 0 0 0 3.7 8.1 2.5 2.5 0 0 0 4.5 13z"/>'
        ),
    },
]


def encode_icon(filename: str) -> str:
    """Base64-encode a local PNG or SVG icon as a data URI."""
    path = ICON_DIR / filename
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/svg+xml" if filename.endswith(".svg") else "image/png"
    return f"data:{mime};base64,{b64}"


STATUS_STYLES = {
    "Active": {
        "bg": "#dcfce7",
        "fg": "#166534",
        "dot": "#22c55e",
        "width": 64,
    },
    "In Progress": {
        "bg": "#dbeafe",
        "fg": "#1e40af",
        "dot": "#3b82f6",
        "width": 96,
    },
    "Discontinued": {
        "bg": "#f1f5f9",
        "fg": "#475569",
        "dot": "#94a3b8",
        "width": 104,
    },
}


def make_svg(card: dict) -> str:
    """Render a self-contained 420x144 SVG card for the given project metadata."""
    data_uri = encode_icon(card["icon"])
    g1, g2 = card["grad"]
    title = html.escape(card["title"])
    subtitle = html.escape(card["subtitle"])
    created = html.escape(card["created"])
    stack = html.escape(card["stack"])
    status_label = card["status"]
    style = STATUS_STYLES[status_label]

    badge_bg = style["bg"]
    badge_fg = style["fg"]
    dot_fg = style["dot"]
    badge_w = style["width"]

    if card["mode"] == "bleed":
        art = f'<image href="{data_uri}" x="248" y="-10" width="168" height="168" preserveAspectRatio="xMidYMid meet" />'
    else:
        art = f'<image href="{data_uri}" x="278" y="20" width="112" height="104" preserveAspectRatio="xMidYMid meet" />'

    badge_x = 80
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="144" viewBox="0 0 420 144" role="img" aria-label="{title} - {subtitle} ({created})">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{g1}"/>
      <stop offset="100%" stop-color="{g2}"/>
    </linearGradient>
    <clipPath id="cardClip">
      <rect x="0" y="0" width="420" height="144" rx="16" ry="16"/>
    </clipPath>
  </defs>
  <g clip-path="url(#cardClip)">
    <rect x="0" y="0" width="420" height="144" fill="url(#bg)"/>
    {art}
    <text x="24" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="21" font-weight="700" fill="#1e293b">{title}</text>
    <text x="24" y="61" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="13" font-weight="500" fill="#64748b">{subtitle}</text>
    <text x="24" y="81" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11" font-weight="500" fill="#94a3b8">{stack}</text>
    <text x="24" y="113" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11.5" font-weight="600" fill="#64748b">{created}</text>
    <rect x="{badge_x}" y="98" width="{badge_w}" height="22" rx="11" fill="{badge_bg}"/>
    <circle cx="{badge_x + 11}" cy="109" r="3.5" fill="{dot_fg}"/>
    <text x="{badge_x + 20}" y="113" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11" font-weight="600" fill="{badge_fg}">{status_label}</text>
  </g>
  <rect x="0.5" y="0.5" width="419" height="143" rx="15.5" ry="15.5" fill="none" stroke="#cbd5e1" stroke-opacity="0.65"/>
</svg>'''


def make_focus_svg(card: dict) -> str:
    """Render a compact 420x96 SVG card for an engineering focus pillar."""
    g1, g2 = card["grad"]
    title = html.escape(card["title"])
    desc = html.escape(card["desc"])
    meta = html.escape(card["meta"])
    badge_bg = card["badge_bg"]
    accent = card["accent"]
    icon_svg = card["icon_svg"]
    font = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="96" viewBox="0 0 420 96" role="img" aria-label="{title} - {desc}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{g1}"/>
      <stop offset="100%" stop-color="{g2}"/>
    </linearGradient>
    <clipPath id="cardClip">
      <rect x="0" y="0" width="420" height="96" rx="16" ry="16"/>
    </clipPath>
  </defs>
  <g clip-path="url(#cardClip)">
    <rect x="0" y="0" width="420" height="96" fill="url(#bg)"/>
    <rect x="20" y="30" width="36" height="36" rx="10" fill="{badge_bg}"/>
    <g transform="translate(30, 40)" fill="none" stroke="{accent}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      {icon_svg}
    </g>
    <text x="72" y="36" font-family="{font}" font-size="16" font-weight="700" fill="#1e293b">{title}</text>
    <text x="72" y="57" font-family="{font}" font-size="12.5" font-weight="500" fill="#64748b">{desc}</text>
    <text x="72" y="75" font-family="{font}" font-size="11" font-weight="500" fill="#94a3b8">{meta}</text>
  </g>
  <rect x="0.5" y="0.5" width="419" height="95" rx="15.5" ry="15.5" fill="none" stroke="#cbd5e1" stroke-opacity="0.65"/>
</svg>'''


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for card in CARDS:
        out_path = OUT_DIR / f"{card['id']}.svg"
        out_path.write_text(make_svg(card), encoding="utf-8")
        print(f"Generated: {out_path.relative_to(ROOT_DIR)}")
    for card in FOCUS_CARDS:
        out_path = OUT_DIR / f"{card['id']}.svg"
        out_path.write_text(make_focus_svg(card), encoding="utf-8")
        print(f"Generated: {out_path.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()
