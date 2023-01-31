from PIL import Image

sprava = 'blabla #'
obr = Image.open("nature.png")
pixels = obr.load()


def priprav(sprava:str)->list:
    res =[]
    for pismenko in sprava:
        cislo = bin(ord(pismenko))[2::].zfill(8)
        for j in cislo:
            res.append(int(j))
    return res

def drticka(sprava):
    spvds = priprav(sprava)
    sirka = obr.size[0]
    for i in range(len(spvds)):
        x = i % sirka
        y = i // sirka
        pixelblue = pixels[x,y][2]
        #print(pixel)
        binstr = bin(pixelblue)
        str2 = binstr[2:-1:]
        newblue=int(str2 + str(spvds[i]),2)
        newcolour = (pixels[x,y][0],pixels[x,y][1],newblue)
        print(pixels[x,y],newcolour)
        pixels[x, y] = newcolour
    obr.save("obrsospr.png")

def skladacka()->str:
    list = []
    obr2 = Image.open("obrsospr.png")
    pixels2 = obr2.load()
    sirka,vyska = obr2.size
    for y in range(vyska):
        for x in range(sirka):
            blue = pixels2[x,y][2]
            biners = bin(blue)[-1::]
            list.append(int(biners))
    return dekoduj(list)

def dekoduj(list)->str:
    text = ""
    for j in range(0,len(list),8):
        pismenko = ""
        for i in range(8):
            pismenko += str(list[j+i])
        ch = chr(int(pismenko,2))
        text+=ch
        if ch == "#":
            break
    return text
print(priprav(sprava))
drticka(sprava)
print(skladacka())
