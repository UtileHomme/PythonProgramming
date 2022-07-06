import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# Searching for abc
pattern = re.compile('abc')

matches = pattern.finditer(text_to_search)

# span is the beginning and ending index of the match
# <re.Match object; span=(1, 4), match='abc'>
# for match in matches:
#     print(match)

# Searching for escaped sequences - a dot
pattern = re.compile(r'\.')

matches = pattern.finditer(text_to_search)

# span is the beginning and ending index of the match
# <re.Match object; span=(113, 114), match='.'>
# <re.Match object; span=(149, 150), match='.'>
# <re.Match object; span=(171, 172), match='.'>
# <re.Match object; span=(175, 176), match='.'>
# <re.Match object; span=(223, 224), match='.'>
# <re.Match object; span=(254, 255), match='.'>
# <re.Match object; span=(267, 268), match='.'>
# for match in matches:
#     print(match)

# Searching for escaped sequences - string and a dot
pattern = re.compile(r'coreyms\.com')

matches = pattern.finditer(text_to_search)

# span is the beginning and ending index of the match
# <re.Match object; span=(142, 153), match='coreyms.com'>
# for match in matches:
#     print(match)

# Searching for all characters except a new line
pattern = re.compile(r'.')

matches = pattern.finditer(text_to_search)

# span is the beginning and ending index of the match
# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='b'>
# <re.Match object; span=(3, 4), match='c'>
# <re.Match object; span=(4, 5), match='d'>
# <re.Match object; span=(5, 6), match='e'>
# <re.Match object; span=(6, 7), match='f'>
# <re.Match object; span=(7, 8), match='g'>
# <re.Match object; span=(8, 9), match='h'>
# <re.Match object; span=(9, 10), match='i'>
# <re.Match object; span=(10, 11), match='j'>
# <re.Match object; span=(11, 12), match='k'>
# <re.Match object; span=(12, 13), match='l'>
# <re.Match object; span=(13, 14), match='m'>
# <re.Match object; span=(14, 15), match='n'>
# <re.Match object; span=(15, 16), match='o'>
# <re.Match object; span=(16, 17), match='p'>
# <re.Match object; span=(17, 18), match='q'>
# <re.Match object; span=(18, 19), match='u'>
# <re.Match object; span=(19, 20), match='r'>
# <re.Match object; span=(20, 21), match='t'>
# <re.Match object; span=(21, 22), match='u'>
# <re.Match object; span=(22, 23), match='v'>
# <re.Match object; span=(23, 24), match='w'>
# <re.Match object; span=(24, 25), match='x'>
# <re.Match object; span=(25, 26), match='y'>
# <re.Match object; span=(26, 27), match='z'>
# <re.Match object; span=(28, 29), match='A'>
# <re.Match object; span=(29, 30), match='B'>
# <re.Match object; span=(30, 31), match='C'>
# <re.Match object; span=(31, 32), match='D'>
# <re.Match object; span=(32, 33), match='E'>
# <re.Match object; span=(33, 34), match='F'>
# <re.Match object; span=(34, 35), match='G'>
# <re.Match object; span=(35, 36), match='H'>
# <re.Match object; span=(36, 37), match='I'>
# <re.Match object; span=(37, 38), match='J'>
# <re.Match object; span=(38, 39), match='K'>
# <re.Match object; span=(39, 40), match='L'>
# <re.Match object; span=(40, 41), match='M'>
# <re.Match object; span=(41, 42), match='N'>
# <re.Match object; span=(42, 43), match='O'>
# <re.Match object; span=(43, 44), match='P'>
# <re.Match object; span=(44, 45), match='Q'>
# <re.Match object; span=(45, 46), match='R'>
# <re.Match object; span=(46, 47), match='S'>
# <re.Match object; span=(47, 48), match='T'>
# <re.Match object; span=(48, 49), match='U'>
# <re.Match object; span=(49, 50), match='V'>
# <re.Match object; span=(50, 51), match='W'>
# <re.Match object; span=(51, 52), match='X'>
# <re.Match object; span=(52, 53), match='Y'>
# <re.Match object; span=(53, 54), match='Z'>
# <re.Match object; span=(55, 56), match='1'>
# <re.Match object; span=(56, 57), match='2'>
# <re.Match object; span=(57, 58), match='3'>
# <re.Match object; span=(58, 59), match='4'>
# <re.Match object; span=(59, 60), match='5'>
# <re.Match object; span=(60, 61), match='6'>
# <re.Match object; span=(61, 62), match='7'>
# <re.Match object; span=(62, 63), match='8'>
# <re.Match object; span=(63, 64), match='9'>
# <re.Match object; span=(64, 65), match='0'>
# <re.Match object; span=(67, 68), match='H'>
# <re.Match object; span=(68, 69), match='a'>
# <re.Match object; span=(69, 70), match=' '>
# <re.Match object; span=(70, 71), match='H'>
# <re.Match object; span=(71, 72), match='a'>
# <re.Match object; span=(72, 73), match='H'>
# <re.Match object; span=(73, 74), match='a'>
# <re.Match object; span=(76, 77), match='M'>
# <re.Match object; span=(77, 78), match='e'>
# <re.Match object; span=(78, 79), match='t'>
# <re.Match object; span=(79, 80), match='a'>
# <re.Match object; span=(80, 81), match='C'>
# <re.Match object; span=(81, 82), match='h'>
# <re.Match object; span=(82, 83), match='a'>
# <re.Match object; span=(83, 84), match='r'>
# <re.Match object; span=(84, 85), match='a'>
# <re.Match object; span=(85, 86), match='c'>
# <re.Match object; span=(86, 87), match='t'>
# <re.Match object; span=(87, 88), match='e'>
# <re.Match object; span=(88, 89), match='r'>
# <re.Match object; span=(89, 90), match='s'>
# <re.Match object; span=(90, 91), match=' '>
# <re.Match object; span=(91, 92), match='('>
# <re.Match object; span=(92, 93), match='N'>
# <re.Match object; span=(93, 94), match='e'>
# <re.Match object; span=(94, 95), match='e'>
# <re.Match object; span=(95, 96), match='d'>
# <re.Match object; span=(96, 97), match=' '>
# <re.Match object; span=(97, 98), match='t'>
# <re.Match object; span=(98, 99), match='o'>
# <re.Match object; span=(99, 100), match=' '>
# <re.Match object; span=(100, 101), match='b'>
# <re.Match object; span=(101, 102), match='e'>
# <re.Match object; span=(102, 103), match=' '>
# <re.Match object; span=(103, 104), match='e'>
# <re.Match object; span=(104, 105), match='s'>
# <re.Match object; span=(105, 106), match='c'>
# <re.Match object; span=(106, 107), match='a'>
# <re.Match object; span=(107, 108), match='p'>
# <re.Match object; span=(108, 109), match='e'>
# <re.Match object; span=(109, 110), match='d'>
# <re.Match object; span=(110, 111), match=')'>
# <re.Match object; span=(111, 112), match=':'>
# <re.Match object; span=(113, 114), match='.'>
# <re.Match object; span=(114, 115), match=' '>
# <re.Match object; span=(115, 116), match='^'>
# <re.Match object; span=(116, 117), match=' '>
# <re.Match object; span=(117, 118), match='$'>
# <re.Match object; span=(118, 119), match=' '>
# <re.Match object; span=(119, 120), match='*'>
# <re.Match object; span=(120, 121), match=' '>
# <re.Match object; span=(121, 122), match='+'>
# <re.Match object; span=(122, 123), match=' '>
# <re.Match object; span=(123, 124), match='?'>
# <re.Match object; span=(124, 125), match=' '>
# <re.Match object; span=(125, 126), match='{'>
# <re.Match object; span=(126, 127), match=' '>
# <re.Match object; span=(127, 128), match='}'>
# <re.Match object; span=(128, 129), match=' '>
# <re.Match object; span=(129, 130), match='['>
# <re.Match object; span=(130, 131), match=' '>
# <re.Match object; span=(131, 132), match=']'>
# <re.Match object; span=(132, 133), match=' '>
# <re.Match object; span=(133, 134), match='\\'>
# <re.Match object; span=(134, 135), match=' '>
# <re.Match object; span=(135, 136), match='|'>
# <re.Match object; span=(136, 137), match=' '>
# <re.Match object; span=(137, 138), match='('>
# <re.Match object; span=(138, 139), match=' '>
# <re.Match object; span=(139, 140), match=')'>
# <re.Match object; span=(142, 143), match='c'>
# <re.Match object; span=(143, 144), match='o'>
# <re.Match object; span=(144, 145), match='r'>
# <re.Match object; span=(145, 146), match='e'>
# <re.Match object; span=(146, 147), match='y'>
# <re.Match object; span=(147, 148), match='m'>
# <re.Match object; span=(148, 149), match='s'>
# <re.Match object; span=(149, 150), match='.'>
# <re.Match object; span=(150, 151), match='c'>
# <re.Match object; span=(151, 152), match='o'>
# <re.Match object; span=(152, 153), match='m'>
# <re.Match object; span=(155, 156), match='3'>
# <re.Match object; span=(156, 157), match='2'>
# <re.Match object; span=(157, 158), match='1'>
# <re.Match object; span=(158, 159), match='-'>
# <re.Match object; span=(159, 160), match='5'>
# <re.Match object; span=(160, 161), match='5'>
# <re.Match object; span=(161, 162), match='5'>
# <re.Match object; span=(162, 163), match='-'>
# <re.Match object; span=(163, 164), match='4'>
# <re.Match object; span=(164, 165), match='3'>
# <re.Match object; span=(165, 166), match='2'>
# <re.Match object; span=(166, 167), match='1'>
# <re.Match object; span=(168, 169), match='1'>
# <re.Match object; span=(169, 170), match='2'>
# <re.Match object; span=(170, 171), match='3'>
# <re.Match object; span=(171, 172), match='.'>
# <re.Match object; span=(172, 173), match='5'>
# <re.Match object; span=(173, 174), match='5'>
# <re.Match object; span=(174, 175), match='5'>
# <re.Match object; span=(175, 176), match='.'>
# <re.Match object; span=(176, 177), match='1'>
# <re.Match object; span=(177, 178), match='2'>
# <re.Match object; span=(178, 179), match='3'>
# <re.Match object; span=(179, 180), match='4'>
# <re.Match object; span=(181, 182), match='1'>
# <re.Match object; span=(182, 183), match='2'>
# <re.Match object; span=(183, 184), match='3'>
# <re.Match object; span=(184, 185), match='*'>
# <re.Match object; span=(185, 186), match='5'>
# <re.Match object; span=(186, 187), match='5'>
# <re.Match object; span=(187, 188), match='5'>
# <re.Match object; span=(188, 189), match='*'>
# <re.Match object; span=(189, 190), match='1'>
# <re.Match object; span=(190, 191), match='2'>
# <re.Match object; span=(191, 192), match='3'>
# <re.Match object; span=(192, 193), match='4'>
# <re.Match object; span=(194, 195), match='8'>
# <re.Match object; span=(195, 196), match='0'>
# <re.Match object; span=(196, 197), match='0'>
# <re.Match object; span=(197, 198), match='-'>
# <re.Match object; span=(198, 199), match='5'>
# <re.Match object; span=(199, 200), match='5'>
# <re.Match object; span=(200, 201), match='5'>
# <re.Match object; span=(201, 202), match='-'>
# <re.Match object; span=(202, 203), match='1'>
# <re.Match object; span=(203, 204), match='2'>
# <re.Match object; span=(204, 205), match='3'>
# <re.Match object; span=(205, 206), match='4'>
# <re.Match object; span=(207, 208), match='9'>
# <re.Match object; span=(208, 209), match='0'>
# <re.Match object; span=(209, 210), match='0'>
# <re.Match object; span=(210, 211), match='-'>
# <re.Match object; span=(211, 212), match='5'>
# <re.Match object; span=(212, 213), match='5'>
# <re.Match object; span=(213, 214), match='5'>
# <re.Match object; span=(214, 215), match='-'>
# <re.Match object; span=(215, 216), match='1'>
# <re.Match object; span=(216, 217), match='2'>
# <re.Match object; span=(217, 218), match='3'>
# <re.Match object; span=(218, 219), match='4'>
# <re.Match object; span=(221, 222), match='M'>
# <re.Match object; span=(222, 223), match='r'>
# <re.Match object; span=(223, 224), match='.'>
# <re.Match object; span=(224, 225), match=' '>
# <re.Match object; span=(225, 226), match='S'>
# <re.Match object; span=(226, 227), match='c'>
# <re.Match object; span=(227, 228), match='h'>
# <re.Match object; span=(228, 229), match='a'>
# <re.Match object; span=(229, 230), match='f'>
# <re.Match object; span=(230, 231), match='e'>
# <re.Match object; span=(231, 232), match='r'>
# <re.Match object; span=(233, 234), match='M'>
# <re.Match object; span=(234, 235), match='r'>
# <re.Match object; span=(235, 236), match=' '>
# <re.Match object; span=(236, 237), match='S'>
# <re.Match object; span=(237, 238), match='m'>
# <re.Match object; span=(238, 239), match='i'>
# <re.Match object; span=(239, 240), match='t'>
# <re.Match object; span=(240, 241), match='h'>
# <re.Match object; span=(242, 243), match='M'>
# <re.Match object; span=(243, 244), match='s'>
# <re.Match object; span=(244, 245), match=' '>
# <re.Match object; span=(245, 246), match='D'>
# <re.Match object; span=(246, 247), match='a'>
# <re.Match object; span=(247, 248), match='v'>
# <re.Match object; span=(248, 249), match='i'>
# <re.Match object; span=(249, 250), match='s'>
# <re.Match object; span=(251, 252), match='M'>
# <re.Match object; span=(252, 253), match='r'>
# <re.Match object; span=(253, 254), match='s'>
# <re.Match object; span=(254, 255), match='.'>
# <re.Match object; span=(255, 256), match=' '>
# <re.Match object; span=(256, 257), match='R'>
# <re.Match object; span=(257, 258), match='o'>
# <re.Match object; span=(258, 259), match='b'>
# <re.Match object; span=(259, 260), match='i'>
# <re.Match object; span=(260, 261), match='n'>
# <re.Match object; span=(261, 262), match='s'>
# <re.Match object; span=(262, 263), match='o'>
# <re.Match object; span=(263, 264), match='n'>
# <re.Match object; span=(265, 266), match='M'>
# <re.Match object; span=(266, 267), match='r'>
# <re.Match object; span=(267, 268), match='.'>
# <re.Match object; span=(268, 269), match=' '>
# <re.Match object; span=(269, 270), match='T'>
# for match in matches:
#     print(match)

# Searching for digits
# \d      - Digit (0-9)
pattern = re.compile('\d')

matches = pattern.finditer(text_to_search)

# span is the beginning and ending index of the match
# <re.Match object; span=(55, 56), match='1'>
# <re.Match object; span=(56, 57), match='2'>
# <re.Match object; span=(57, 58), match='3'>
# <re.Match object; span=(58, 59), match='4'>
# <re.Match object; span=(59, 60), match='5'>
# <re.Match object; span=(60, 61), match='6'>
# <re.Match object; span=(61, 62), match='7'>
# <re.Match object; span=(62, 63), match='8'>
# <re.Match object; span=(63, 64), match='9'>
# <re.Match object; span=(64, 65), match='0'>
# <re.Match object; span=(155, 156), match='3'>
# <re.Match object; span=(156, 157), match='2'>
# <re.Match object; span=(157, 158), match='1'>
# <re.Match object; span=(159, 160), match='5'>
# <re.Match object; span=(160, 161), match='5'>
# <re.Match object; span=(161, 162), match='5'>
# <re.Match object; span=(163, 164), match='4'>
# <re.Match object; span=(164, 165), match='3'>
# <re.Match object; span=(165, 166), match='2'>
# <re.Match object; span=(166, 167), match='1'>
# <re.Match object; span=(168, 169), match='1'>
# <re.Match object; span=(169, 170), match='2'>
# <re.Match object; span=(170, 171), match='3'>
# <re.Match object; span=(172, 173), match='5'>
# <re.Match object; span=(173, 174), match='5'>
# <re.Match object; span=(174, 175), match='5'>
# <re.Match object; span=(176, 177), match='1'>
# <re.Match object; span=(177, 178), match='2'>
# <re.Match object; span=(178, 179), match='3'>
# <re.Match object; span=(179, 180), match='4'>
# <re.Match object; span=(181, 182), match='1'>
# <re.Match object; span=(182, 183), match='2'>
# <re.Match object; span=(183, 184), match='3'>
# <re.Match object; span=(185, 186), match='5'>
# <re.Match object; span=(186, 187), match='5'>
# <re.Match object; span=(187, 188), match='5'>
# <re.Match object; span=(189, 190), match='1'>
# <re.Match object; span=(190, 191), match='2'>
# <re.Match object; span=(191, 192), match='3'>
# <re.Match object; span=(192, 193), match='4'>
# <re.Match object; span=(194, 195), match='8'>
# <re.Match object; span=(195, 196), match='0'>
# <re.Match object; span=(196, 197), match='0'>
# <re.Match object; span=(198, 199), match='5'>
# <re.Match object; span=(199, 200), match='5'>
# <re.Match object; span=(200, 201), match='5'>
# <re.Match object; span=(202, 203), match='1'>
# <re.Match object; span=(203, 204), match='2'>
# <re.Match object; span=(204, 205), match='3'>
# <re.Match object; span=(205, 206), match='4'>
# <re.Match object; span=(207, 208), match='9'>
# <re.Match object; span=(208, 209), match='0'>
# <re.Match object; span=(209, 210), match='0'>
# <re.Match object; span=(211, 212), match='5'>
# <re.Match object; span=(212, 213), match='5'>
# <re.Match object; span=(213, 214), match='5'>
# <re.Match object; span=(215, 216), match='1'>
# <re.Match object; span=(216, 217), match='2'>
# <re.Match object; span=(217, 218), match='3'>
# <re.Match object; span=(218, 219), match='4'>

# for match in matches:
#     print(match)

# Searching for everything but no digit
# \D      - Not a Digit (0-9)
pattern = re.compile(r'\D')

matches = pattern.finditer(text_to_search)

# span is the beginning and ending index of the match
# <re.Match object; span=(0, 1), match='\n'>
# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='b'>
# <re.Match object; span=(3, 4), match='c'>
# <re.Match object; span=(4, 5), match='d'>
# <re.Match object; span=(5, 6), match='e'>
# <re.Match object; span=(6, 7), match='f'>
# <re.Match object; span=(7, 8), match='g'>
# <re.Match object; span=(8, 9), match='h'>
# <re.Match object; span=(9, 10), match='i'>
# <re.Match object; span=(10, 11), match='j'>
# <re.Match object; span=(11, 12), match='k'>
# <re.Match object; span=(12, 13), match='l'>
# <re.Match object; span=(13, 14), match='m'>
# <re.Match object; span=(14, 15), match='n'>
# <re.Match object; span=(15, 16), match='o'>
# <re.Match object; span=(16, 17), match='p'>
# <re.Match object; span=(17, 18), match='q'>
# <re.Match object; span=(18, 19), match='u'>
# <re.Match object; span=(19, 20), match='r'>
# <re.Match object; span=(20, 21), match='t'>
# <re.Match object; span=(21, 22), match='u'>
# <re.Match object; span=(22, 23), match='v'>
# <re.Match object; span=(23, 24), match='w'>
# <re.Match object; span=(24, 25), match='x'>
# <re.Match object; span=(25, 26), match='y'>
# <re.Match object; span=(26, 27), match='z'>
# <re.Match object; span=(27, 28), match='\n'>
# <re.Match object; span=(28, 29), match='A'>
# <re.Match object; span=(29, 30), match='B'>
# <re.Match object; span=(30, 31), match='C'>
# <re.Match object; span=(31, 32), match='D'>
# <re.Match object; span=(32, 33), match='E'>
# <re.Match object; span=(33, 34), match='F'>
# <re.Match object; span=(34, 35), match='G'>
# <re.Match object; span=(35, 36), match='H'>
# <re.Match object; span=(36, 37), match='I'>
# <re.Match object; span=(37, 38), match='J'>
# <re.Match object; span=(38, 39), match='K'>
# <re.Match object; span=(39, 40), match='L'>
# <re.Match object; span=(40, 41), match='M'>
# <re.Match object; span=(41, 42), match='N'>
# <re.Match object; span=(42, 43), match='O'>
# <re.Match object; span=(43, 44), match='P'>
# <re.Match object; span=(44, 45), match='Q'>
# <re.Match object; span=(45, 46), match='R'>
# <re.Match object; span=(46, 47), match='S'>
# <re.Match object; span=(47, 48), match='T'>
# <re.Match object; span=(48, 49), match='U'>
# <re.Match object; span=(49, 50), match='V'>
# <re.Match object; span=(50, 51), match='W'>
# <re.Match object; span=(51, 52), match='X'>
# <re.Match object; span=(52, 53), match='Y'>
# <re.Match object; span=(53, 54), match='Z'>
# <re.Match object; span=(54, 55), match='\n'>
# <re.Match object; span=(65, 66), match='\n'>
# <re.Match object; span=(66, 67), match='\n'>
# <re.Match object; span=(67, 68), match='H'>
# <re.Match object; span=(68, 69), match='a'>
# <re.Match object; span=(69, 70), match=' '>
# <re.Match object; span=(70, 71), match='H'>
# <re.Match object; span=(71, 72), match='a'>
# <re.Match object; span=(72, 73), match='H'>
# <re.Match object; span=(73, 74), match='a'>
# <re.Match object; span=(74, 75), match='\n'>
# <re.Match object; span=(75, 76), match='\n'>
# <re.Match object; span=(76, 77), match='M'>
# <re.Match object; span=(77, 78), match='e'>
# <re.Match object; span=(78, 79), match='t'>
# <re.Match object; span=(79, 80), match='a'>
# <re.Match object; span=(80, 81), match='C'>
# <re.Match object; span=(81, 82), match='h'>
# <re.Match object; span=(82, 83), match='a'>
# <re.Match object; span=(83, 84), match='r'>
# <re.Match object; span=(84, 85), match='a'>
# <re.Match object; span=(85, 86), match='c'>
# <re.Match object; span=(86, 87), match='t'>
# <re.Match object; span=(87, 88), match='e'>
# <re.Match object; span=(88, 89), match='r'>
# <re.Match object; span=(89, 90), match='s'>
# <re.Match object; span=(90, 91), match=' '>
# <re.Match object; span=(91, 92), match='('>
# <re.Match object; span=(92, 93), match='N'>
# <re.Match object; span=(93, 94), match='e'>
# <re.Match object; span=(94, 95), match='e'>
# <re.Match object; span=(95, 96), match='d'>
# <re.Match object; span=(96, 97), match=' '>
# <re.Match object; span=(97, 98), match='t'>
# <re.Match object; span=(98, 99), match='o'>
# <re.Match object; span=(99, 100), match=' '>
# <re.Match object; span=(100, 101), match='b'>
# <re.Match object; span=(101, 102), match='e'>
# <re.Match object; span=(102, 103), match=' '>
# <re.Match object; span=(103, 104), match='e'>
# <re.Match object; span=(104, 105), match='s'>
# <re.Match object; span=(105, 106), match='c'>
# <re.Match object; span=(106, 107), match='a'>
# <re.Match object; span=(107, 108), match='p'>
# <re.Match object; span=(108, 109), match='e'>
# <re.Match object; span=(109, 110), match='d'>
# <re.Match object; span=(110, 111), match=')'>
# <re.Match object; span=(111, 112), match=':'>
# <re.Match object; span=(112, 113), match='\n'>
# <re.Match object; span=(113, 114), match='.'>
# <re.Match object; span=(114, 115), match=' '>
# <re.Match object; span=(115, 116), match='^'>
# <re.Match object; span=(116, 117), match=' '>
# <re.Match object; span=(117, 118), match='$'>
# <re.Match object; span=(118, 119), match=' '>
# <re.Match object; span=(119, 120), match='*'>
# <re.Match object; span=(120, 121), match=' '>
# <re.Match object; span=(121, 122), match='+'>
# <re.Match object; span=(122, 123), match=' '>
# <re.Match object; span=(123, 124), match='?'>
# <re.Match object; span=(124, 125), match=' '>
# <re.Match object; span=(125, 126), match='{'>
# <re.Match object; span=(126, 127), match=' '>
# <re.Match object; span=(127, 128), match='}'>
# <re.Match object; span=(128, 129), match=' '>
# <re.Match object; span=(129, 130), match='['>
# <re.Match object; span=(130, 131), match=' '>
# <re.Match object; span=(131, 132), match=']'>
# <re.Match object; span=(132, 133), match=' '>
# <re.Match object; span=(133, 134), match='\\'>
# <re.Match object; span=(134, 135), match=' '>
# <re.Match object; span=(135, 136), match='|'>
# <re.Match object; span=(136, 137), match=' '>
# <re.Match object; span=(137, 138), match='('>
# <re.Match object; span=(138, 139), match=' '>
# <re.Match object; span=(139, 140), match=')'>
# <re.Match object; span=(140, 141), match='\n'>
# <re.Match object; span=(141, 142), match='\n'>
# <re.Match object; span=(142, 143), match='c'>
# <re.Match object; span=(143, 144), match='o'>
# <re.Match object; span=(144, 145), match='r'>
# <re.Match object; span=(145, 146), match='e'>
# <re.Match object; span=(146, 147), match='y'>
# <re.Match object; span=(147, 148), match='m'>
# <re.Match object; span=(148, 149), match='s'>
# <re.Match object; span=(149, 150), match='.'>
# <re.Match object; span=(150, 151), match='c'>
# <re.Match object; span=(151, 152), match='o'>
# <re.Match object; span=(152, 153), match='m'>
# <re.Match object; span=(153, 154), match='\n'>
# <re.Match object; span=(154, 155), match='\n'>
# <re.Match object; span=(158, 159), match='-'>
# <re.Match object; span=(162, 163), match='-'>
# <re.Match object; span=(167, 168), match='\n'>
# <re.Match object; span=(171, 172), match='.'>
# <re.Match object; span=(175, 176), match='.'>
# <re.Match object; span=(180, 181), match='\n'>
# <re.Match object; span=(184, 185), match='*'>
# <re.Match object; span=(188, 189), match='*'>
# <re.Match object; span=(193, 194), match='\n'>
# <re.Match object; span=(197, 198), match='-'>
# <re.Match object; span=(201, 202), match='-'>
# <re.Match object; span=(206, 207), match='\n'>
# <re.Match object; span=(210, 211), match='-'>
# <re.Match object; span=(214, 215), match='-'>
# <re.Match object; span=(219, 220), match='\n'>
# <re.Match object; span=(220, 221), match='\n'>
# <re.Match object; span=(221, 222), match='M'>
# <re.Match object; span=(222, 223), match='r'>
# <re.Match object; span=(223, 224), match='.'>
# <re.Match object; span=(224, 225), match=' '>
# <re.Match object; span=(225, 226), match='S'>
# <re.Match object; span=(226, 227), match='c'>
# <re.Match object; span=(227, 228), match='h'>
# <re.Match object; span=(228, 229), match='a'>
# <re.Match object; span=(229, 230), match='f'>
# <re.Match object; span=(230, 231), match='e'>
# <re.Match object; span=(231, 232), match='r'>
# <re.Match object; span=(232, 233), match='\n'>
# <re.Match object; span=(233, 234), match='M'>
# <re.Match object; span=(234, 235), match='r'>
# <re.Match object; span=(235, 236), match=' '>
# <re.Match object; span=(236, 237), match='S'>
# <re.Match object; span=(237, 238), match='m'>
# <re.Match object; span=(238, 239), match='i'>
# <re.Match object; span=(239, 240), match='t'>
# <re.Match object; span=(240, 241), match='h'>
# <re.Match object; span=(241, 242), match='\n'>
# <re.Match object; span=(242, 243), match='M'>
# <re.Match object; span=(243, 244), match='s'>
# <re.Match object; span=(244, 245), match=' '>
# <re.Match object; span=(245, 246), match='D'>
# <re.Match object; span=(246, 247), match='a'>
# <re.Match object; span=(247, 248), match='v'>
# <re.Match object; span=(248, 249), match='i'>
# <re.Match object; span=(249, 250), match='s'>
# <re.Match object; span=(250, 251), match='\n'>
# <re.Match object; span=(251, 252), match='M'>
# <re.Match object; span=(252, 253), match='r'>
# <re.Match object; span=(253, 254), match='s'>
# <re.Match object; span=(254, 255), match='.'>
# <re.Match object; span=(255, 256), match=' '>
# <re.Match object; span=(256, 257), match='R'>
# <re.Match object; span=(257, 258), match='o'>
# <re.Match object; span=(258, 259), match='b'>
# <re.Match object; span=(259, 260), match='i'>
# <re.Match object; span=(260, 261), match='n'>
# <re.Match object; span=(261, 262), match='s'>
# <re.Match object; span=(262, 263), match='o'>
# <re.Match object; span=(263, 264), match='n'>
# <re.Match object; span=(264, 265), match='\n'>
# <re.Match object; span=(265, 266), match='M'>
# <re.Match object; span=(266, 267), match='r'>
# <re.Match object; span=(267, 268), match='.'>
# <re.Match object; span=(268, 269), match=' '>
# <re.Match object; span=(269, 270), match='T'>
# <re.Match object; span=(270, 271), match='\n'>

# for match in matches:
#     print(match)

# Match a word character
# \w      - Word Character (a-z, A-Z, 0-9, _)
pattern = re.compile(r'\w')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Match a NOT word character
# \W      - Not a Word Character
#
pattern = re.compile(r'\W')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# Match a whitespace
# \s      - Whitespace (space, tab, newline)

pattern = re.compile(r'\s')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Match NOT a whitespace
# \S      - Not Whitespace (space, tab, newline)

pattern = re.compile(r'\S')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Match a word boundary
# Ha HaHa
# In this case it will match the first Ha because it is a word boundary and the second Ha
# But it will not match the third Ha because it's part of another word
pattern = re.compile(r'\bHa')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Match NOT a word boundary
# Ha HaHa
# In this case it will match the Third  Ha because it is NOT a word boundary but
# the first and second Ha are word boundaries
pattern = re.compile(r'\BHa')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# ^       - Match Beginning of a String
pattern = re.compile(r'^Start')

matches = pattern.finditer(sentence)

# for match in matches:
#     print(match)

# $       - End of a String
pattern = re.compile(r'end$')

matches = pattern.finditer(sentence)

# for match in matches:
#     print(match)

# How to match Phone number with any character in it
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Parsing data from data.txt file

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#
#
# with open('data.txt','r') as f:
#     contents = f.read()
#
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# How to match Phone number with character set (dot and dash) in it
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# How to match Phone number starting with 8 or 9 and having character set (dot and dash) in it
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# How to match numbers  with range of 1 to 5
pattern = re.compile(r'[1-5]')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# How to match numbers  with range of a to r and A to R
pattern = re.compile(r'[a-rA-R]')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# How to match numbers WHICH ARE NOT with range of a to r and A to R
# In this case, ^ means NOT rather than starting of the string search
pattern = re.compile(r'[^a-rA-R]')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# How to match cat, mat, pat but not bat
# In this case, ^ means NOT rather than starting of the string search
pattern = re.compile(r'[^b]at')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Using Quantifiers to match multiple occurrences
# Match 3 digits, then a dot, then 3 digits then a dot and the 4 digits
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Match for Mr. and Mr
# ?       - 0 or One
# dot after the r is option. We do this using ?
pattern = re.compile(r'Mr\.?')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

# Match for Mr. and Mr (with space) and first uppercase Letter and then other characters
# ?       - 0 or One
# \s      - Whitespace (space, tab, newline)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
pattern = re.compile(r'Mr\.?\s[A-Z]\w+')

matches = pattern.finditer(text_to_search)

# Output

# <re.Match object; span=(221, 232), match='Mr. Schafer'>
# <re.Match object; span=(233, 241), match='Mr Smith'>

# for match in matches:
#     print(match)

# Match for Mr. and Mr (with space) and first uppercase Letter or then other characters
# ?       - 0 or One
# \s      - Whitespace (space, tab, newline)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# *       - 0 or More


pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

# Output
# <re.Match object; span=(221, 232), match='Mr. Schafer'>
# <re.Match object; span=(233, 241), match='Mr Smith'>
# <re.Match object; span=(265, 270), match='Mr. T'>

# for match in matches:
#     print(match)

# Match for Mr. and Mr (with space) and Ms and Ms. and Mrs. and Mrs and first uppercase Letter or then other characters
# ?       - 0 or One
# \s      - Whitespace (space, tab, newline)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# *       - 0 or More
# |       - Either Or
# ( )     - Group
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# OR
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

# Output
# <re.Match object; span=(221, 232), match='Mr. Schafer'>
# <re.Match object; span=(233, 241), match='Mr Smith'>
# <re.Match object; span=(242, 250), match='Ms Davis'>
# <re.Match object; span=(251, 264), match='Mrs. Robinson'>
# <re.Match object; span=(265, 270), match='Mr. T'>

# for match in matches:
#     print(match)



# HOW TO USE FINDALL

# Match for Mr. and Mr (with space) and Ms and Ms. and Mrs. and Mrs and first uppercase Letter or then other characters
# ?       - 0 or One
# \s      - Whitespace (space, tab, newline)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# *       - 0 or More
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w+')

# findall will return a list of strings which match
matches = pattern.findall(text_to_search)

print(matches)

for match in matches:
    print(match)

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# findall will return a list of strings which match
matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

# HOW TO USE MATCH method

pattern = re.compile(r'Start')

# match searches for the match of the string at the starting of the string

matches = pattern.match(sentence)

# <re.Match object; span=(0, 5), match='Start'>
print(matches)

# HOW TO USE search method

# search for first match of the string in the entire string
pattern = re.compile(r'start', re.I)


matches = pattern.search(sentence)

# <re.Match object; span=(0, 5), match='Start'>

# print(matches)

# How to use FLAGs
# re.I will ignore the case and search for start or Start
pattern = re.compile(r'start', re.I)


matches = pattern.search(sentence)

# <re.Match object; span=(0, 5), match='Start'>

print(matches)


