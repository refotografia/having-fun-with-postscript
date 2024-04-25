import random

# Color
c = "05"

X = 0
Y = 0

with open("visual_arcs_rand.ps", mode="a") as file:
    file.writelines(
        "%!PS-Adobe-3.0 EPSF-3.0\n%%DocumentData: Clean7Bit\n%%Origin: 0 0\n"
        "%%BoundingBox: 0 0 2000 3000\n%%LanguageLevel: 1\n%%Pages: 1\n%%Page: 1 1\n"
        f"<< /PageSize [2000 3000] >> setpagedevice\n"
    )
    for n in range(1, 20):
        X += 100
        Y = 0
        for n in range(1, 30):
            Y += 100
            L = random.randint(0,25)
            file.writelines(
                f"{L} setlinewidth\n"
                f"0.{c}0 0.{c}0 0.{c}0 setrgbcolor\n"
                f"{X}.000 {Y}.000 10 0 360 arc\n"
                "stroke\n"
            )
    file.writelines("showpage")