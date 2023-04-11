translation = dict()

translation['I'] = 1
translation['v'] = 5
translation['X'] = 10
translation['L'] = 50
translation['C'] = 100
translation['D'] = 500
translation['M'] = 1000

print(translation)

translation = {}

translation = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

print(translation)

def roman2int(number):
    translation = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    i = 0
    result = 0
    while i < len(number):
        if i + 1 < len(number):
            if translation[number[i]] < translation[number[i + 1]]:
                result -= translation[number[i]]
            else:
                result += translation[number[i]]
        i += 1
    result += translation[number[-1]]
    return result
    
print(roman2int("IV"))
print(roman2int("CDXL"))