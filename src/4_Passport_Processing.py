passports = open("./input/four").read().split("\n\n")

count1 = 0
count2 = 0
fieldNames = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

for passport in passports:
    passport = passport.replace('\n', ' ').split()

    # Comprobacion de si estan todos
    passport_names = [pair.split(':')[0] for pair in passport]
    cond = True
    for field in fieldNames:
        if field not in passport_names:
            cond = False
    if cond:
        count1 += 1
    else:
        continue

    # Comprobacion de si estan todos bien
    passport_dict = {p.split(':')[0]:p.split(':')[1] for p in passport}

    byr = passport_dict['byr']
    iyr = passport_dict['iyr']
    eyr = passport_dict['eyr']
    hgt = passport_dict['hgt']
    hcl = passport_dict['hcl']
    ecl = passport_dict['ecl']
    pid = passport_dict['pid']

    b_byr = byr.isdigit() and len(byr)==4 and int(byr)>=1920 and int(byr)<=2002
    b_iyr = byr.isdigit() and len(iyr)==4 and int(iyr)>=2010 and int(iyr)<=2020
    b_eyr = eyr.isdigit() and len(eyr)==4 and int(eyr)>=2020 and int(eyr)<=2030
    b_hgtA = hgt[-2:] == 'cm' and int(hgt[:-2])>=150 and int(hgt[:-2])<=193
    b_hgtB = hgt[-2:] == 'in' and int(hgt[:-2])>=59 and int(hgt[:-2])<=76
    b_hcl = hcl[0] == '#' and all([(ord(c)>96 and ord(c)<103) or (ord(c)>47 and ord(c)<58) for c in hcl[1:]])
    b_ecl = ecl in ['amb','blu','brn','gry','grn','hzl','oth']
    b_pid = pid.isdigit() and len(pid) == 9

    if all([b_byr, b_iyr, b_eyr, any([b_hgtA, b_hgtB]), b_hcl, b_ecl, b_pid]):
        count2 += 1

print('first half',count1)
print('second half',count2)
