import readline
import sys

print('Attempting to generate webpage for your spot...')

args = sys.argv
if(len(args) < 3):
    print('Missing file name argument: ex. spotgenerator.py [input] [output]')
    sys.exit

print(args[1] + ' -> ' + args[2])

#read in the information from the spot txt file
spotFile = open(args[1], 'r')

bigTitle = spotFile.readline().rstrip()
bgImg = spotFile.readline().rstrip()
dayImg = '<img src="' + spotFile.readline().rstrip() + '" width="100%">'
nightImg = '<img src="' + spotFile.readline().rstrip() + '" width="100%">'
location = spotFile.readline().rstrip()
locationEmbed = spotFile.readline().rstrip().replace('width="600"', 'width="100%"')

pros = []
proTemp = spotFile.readline().rstrip()
while(len(proTemp) != 0):
    pros.append(proTemp)
    proTemp = spotFile.readline().rstrip()

cons = []
conTemp = spotFile.readline().rstrip()
while(len(conTemp) != 0):
    cons.append(conTemp)
    conTemp = spotFile.readline().rstrip()

imgs = []
imgTemp = spotFile.readline().rstrip()
while(len(imgTemp) != 0):
    imgs.append(imgTemp)
    imgTemp = spotFile.readline().rstrip()

spotFile.close()

print('Read ' + bigTitle + ' info!')

#generate HTML for pros, cons, images
prosHTML = ''
for p in pros:
    prosHTML += '<li>' + p + '</li>\n'

consHTML = ''
for c in cons:
    consHTML += '<li>' + c + '</li>\n'

imgsHTML = ''
for i in imgs:
    imgsHTML += '<div class="image-container">'
    imgsHTML += '<img src="' + i + '" class="image-inside-div">'
    imgsHTML += '</div>\n'

#read in the spot page format, copy it to output file
formatFile = open('spotpageformat.html', 'r')
outputFile = open(args[2], 'w')

replaceWords = {
    'REPLACE_BIG_TITLE' : bigTitle,
    'REPLACE_BACKGROUND_URL_STRING' : bgImg,
    'REPLACE_DAYTIME_IMAGE' : dayImg,
    'REPLACE_NIGHTTIME_IMAGE' : nightImg,
    'REPLACE_GOOGLE_MAPS_EMBED' : locationEmbed,
    'REPLACE_LOCATION' : location,
    'REPLACE_LIST_PROS' : prosHTML,
    'REPLACE_LIST_CONS' : consHTML,
    'REPLACE_IMAGES' : imgsHTML
}

formatLine = formatFile.readline().strip()
while(formatLine != '</body>'): #THIS MIGHT CHANGE!!!
    if(formatLine.startswith('REPLACE_')):
        outputFile.write(replaceWords.get(formatLine) + '\n')
    else:
        outputFile.write(formatLine + '\n')
    formatLine = formatFile.readline().strip()

formatFile.close()
outputFile.close()

print('Generated ' + args[2] + '.')

print('Done!')
