from PIL import Image
import requests
from io import BytesIO


def kombiniere_kartenbilder(urls):
    bilder = []
    for url in urls:
        response = requests.get(url)
        bilder.append(Image.open(BytesIO(response.content)))

    breite = sum(b.width for b in bilder)
    höhe = max(b.height for b in bilder)
    kombi = Image.new("RGBA", (breite, höhe))

    x = 0
    for b in bilder:
        kombi.paste(b, (x, 0))
        x += b.width

    return kombi.convert("RGB")


def zahlen_verkleinern(zahl: int) -> str:
    for value, suffix in [(1_000_000_000, "B"), (1_000_000, "M"), (1_000, "K")]:
        if zahl >= value:
            number = zahl / value
            return f"{number:.1f}{suffix}".rstrip("0").rstrip(".")
    return str(zahl)
