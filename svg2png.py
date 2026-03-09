"""SVG → PNG with transparent background. Requires: pip install cairosvg"""
import cairosvg, sys

src = sys.argv[1] if len(sys.argv) > 1 else "avatar.svg"
out = src.replace(".svg", ".png")
cairosvg.svg2png(url=src, write_to=out, output_width=512, output_height=512, background_color="transparent")
print(f"{src} → {out}")
