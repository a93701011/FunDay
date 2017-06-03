TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for word in TILES :
    if word == "||":
        line_end = "\n"
        print("" ,end =line_end)
    else:
        line_end = ""
        print(word ,end =line_end)