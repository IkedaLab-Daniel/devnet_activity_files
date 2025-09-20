def calc_prism_volume(base, height, length):
    volume = (base * height * length) / 2
    return volume

base = int(input("Base: "))
height = int(input("Height: "))
length = int(input("Length: "))


# print(f"The Volumn of prism with base '{base}' and height '{height}' is")

print(calc_prism_volume(base, height, length))

print(f""" 

  Prism Volume Formula:
      
      Base * Height
    -----------------  = Volume
            2
""")

print(""" 
            |
            |
            |
            V
""")

print(f""" 
        {base} * {height} * {length}
    -----------------  = {calc_prism_volume(base, height, length)}
            2
""")