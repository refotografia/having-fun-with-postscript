import random

# Number of lines, curves, etc
N = 50
# Line width
L = 7

with open("visual.ps", mode="a") as file:
    file.writelines(
        "%!PS-Adobe-3.0 EPSF-3.0\n%%DocumentData: Clean7Bit\n%%Origin: 0 0\n"
        "%%BoundingBox: 0 0 2000 3000\n%%LanguageLevel: 1\n%%Pages: 1\n%%Page: 1 1\n"
        f"<< /PageSize [2000 3000] >> setpagedevice\n7{L} setlinewidth\n"
    )
    for n in range(1, N):
        a = random.randint(200, 1800)
        b = random.randint(200, 2800)
        c = random.randint(50, 99)
        d = random.randint(300, 2000)
        e = random.randint(2000, 3000)
        f = random.randint(0, 200)
        file.writelines(
            f"0.{c}0 0.{c}0 0.{c}0 setrgbcolor\n"
            f"{a}.000 {b}.000 moveto\n"
            f"{d}.000 {d - f}.000 {e - f}.000 {e}.000 {2000 - a}.000 {3000 - a}.000 curveto\n"
            "stroke\n"
        )
    file.writelines("showpage")