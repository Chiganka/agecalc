from datetime import datetime

byear = int(input("keso sheikvane sheni dabadebis weli: "))

time = datetime.now().year

print("shen xar " + str(time - byear) + " wlis." )
