import re

def valid_height(height):
    x = re.search('([0-9]+)(cm|in)', height)
    return x and ((x[2] == 'cm' and int(x[1]) >= 150 and int(x[1]) <= 193) or (x[2] == 'in' and int(x[1]) >= 59 and int(x[1]) <= 76))
     
with open('input.txt') as file:
    f = [{x.split(':')[0]: x.strip('\n').split(':')[1] for x in p.replace('\n', ' ').split(' ')} for p in file.read().split('\n\n')]

print(sum([1 if ('byr' in p and 'iyr' in p and 'eyr' in p and 'hgt' in p and 'hcl' in p and 'ecl' in p and 'pid' in p) else 0 for p in f]))

valid = 0
for p in f:
    if 'byr' in p and re.search('[0-9]{4}', p['byr']) and int(p['byr']) >= 1920 and int(p['byr']) <= 2002 \
    and 'iyr' in p and re.search('[0-9]{4}', p['iyr']) and int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020 \
    and 'eyr' in p and re.search('[0-9]{4}', p['eyr']) and int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030 \
    and 'hgt' in p and valid_height(p['hgt']) \
    and 'hcl' in p and re.search('#[0-9a-f]{6}', p['hcl']) \
    and 'ecl' in p and re.search('amb|blu|brn|gry|grn|hzl|oth', p['ecl']) \
    and 'pid' in p and len(p['pid']) == 9 and re.search('[0-9]{9}', p['pid']):
        valid += 1
print(valid)

