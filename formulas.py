import random

# Number of lines, curves, etc
N = 50
# Line width
L = 7

with open("visual_f.ps", mode="a") as file:
    file.writelines(
        "%!PS-Adobe-3.0 EPSF-3.0\n%%DocumentData: Clean7Bit\n%%Origin: 0 0\n"
        "%%BoundingBox: 0 0 2000 3000\n%%LanguageLevel: 1\n%%Pages: 1\n%%Page: 1 1\n"
        f"<< /PageSize [2000 3000] >> setpagedevice\n7{L} setlinewidth\n"
    )
    a = random.randint(200, 1800)
    b = random.randint(200, 2800)
    d = random.randint(500, 800)
    e = random.randint(2000, 2200)
    f = random.randint(50, 200)
    for n in range(1, N):
        a = int(a * 1.02)
        b = int(b * 0.995)
        d = int(d * 1.07)
        e = int(e * 0.99)
        f = int(f * 1.1)
        file.writelines(
            f"0.{random.randint(0, 50)} 0.{random.randint(0, 50)} 0.{random.randint(0, 50)} setrgbcolor\n"
            f"{a}.000 {a}.000 moveto\n"
            f"{d}.000 {d - f}.000 {e - f}.000 {e}.000 {2000 - a}.000 {3000 - a}.000 curveto\n"
            "stroke\n"
        )
    file.writelines("showpage")
