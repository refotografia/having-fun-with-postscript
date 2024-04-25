import random

with open("visual_lines_rand.ps", mode="a") as file:
    file.writelines(
        "%!PS-Adobe-3.0 EPSF-3.0\n%%DocumentData: Clean7Bit\n%%Origin: 0 0\n"
        "%%BoundingBox: 0 0 2000 3000\n%%LanguageLevel: 1\n%%Pages: 1\n%%Page: 1 1\n"
        f"<< /PageSize [2000 3000] >> setpagedevice\n"
        f"1000 1500 moveto\n"
    )
    for n in range(1, 50):
        L = random.randint(0, 50)
        c = random.randint(0, 999)
        X = random.randint(1, 2000)
        Y = random.randint(1, 3000)
        file.writelines(
            f"{L} setlinewidth\n"
            f"0.{c} 0.{c} 0.{c} setrgbcolor\n"
            f"{X} {Y} lineto\n"
            f"stroke\n"
            f"{X} {Y} moveto\n"
        )
    file.writelines("showpage")