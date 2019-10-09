r_string = input();
am_pm = r_string[-2:];
if am_pm=="AM":
    hh=r_string[:2]
    if hh=="12":
        rhh="00";
        ressult=rhh+r_string[2:-2]
        print(ressult)
    else:
        print(r_string[:-2])

else:
    hh = r_string[:2]
    int_cn = int(hh);
    if int_cn==12:
        rhh="12";
    else:
        rhh = int_cn+12;
    uhh = str(rhh);
    ressult = uhh+r_string[2:-2]
    print(ressult)