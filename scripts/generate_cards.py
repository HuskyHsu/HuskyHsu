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
        "stack": "Tauri v2 · React · ESP32",
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
        "stack": "Monkey C · TypeScript · React",
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
        "stack": "React · Infinite Canvas",
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
        "stack": "React · Web Audio",
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
        "stack": "React · Vite · PWA",
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
        "stack": "TypeScript · React",
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
        "stack": "TypeScript · React",
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
        "stack": "React · Tailwind",
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
        "stack": "React · Vite · PWA",
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
        "stack": "Vite · Vanilla JS",
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
        "stack": "TypeScript · React",
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
        "stack": "GAS · LINE Bot",
        "status": "Discontinued",
        "grad": ("#ecfdf5", "#fefce8"),
        "icon": "nooklink_icon.png",
        "mode": "contain",
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
    <rect x="24" y="98" width="{badge_w}" height="22" rx="11" fill="{badge_bg}"/>
    <circle cx="35" cy="109" r="3.5" fill="{dot_fg}"/>
    <text x="44" y="113" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11" font-weight="600" fill="{badge_fg}">{status_label}</text>
    <text x="{24 + badge_w + 10}" y="113" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11.5" font-weight="600" fill="#64748b">{created}</text>
  </g>
  <rect x="0.5" y="0.5" width="419" height="143" rx="15.5" ry="15.5" fill="none" stroke="#cbd5e1" stroke-opacity="0.65"/>
</svg>'''


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for card in CARDS:
        out_path = OUT_DIR / f"{card['id']}.svg"
        out_path.write_text(make_svg(card), encoding="utf-8")
        print(f"Generated: {out_path.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()
