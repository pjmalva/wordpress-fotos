import tinify
from os import makedirs, path, walk

keys = [
    "qWH53l5qsXKCmly05xlh6FwvzxV4p7kB", # 500 - https://tinify.com/dashboard/api#token/hchFKJyW4G0xPYHMW7pHp9q6PtT71mZ9/194tFPOjPZkBz0LI
    "d48zp6MTSQQ66WXJf3pFj1k2Fxh0gGH0", # 212 - https://tinify.com/login?token=jKpRWHFNSKH46jJkd4c7cCV4jvt7ZD1C/zc-zsGBj4&redirect=/dashboard/api&new=true
    "7n6gF47KqSkv50XjHNpkWhHgbhGcKGrb", # 246 - 867 - https://tinify.com/dashboard/api#token/LdZw1rm2wtY53wm0PdXCS4WtjDN8Z5X4/zc-zsGLPHw
]

# source = tinify.from_file("unoptimized.jpg")
# source.to_file("optimized.jpg")

count = 0
for (dirpath, dirname, filenames) in walk('img'):
    for filename in filenames:
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            currentKey = 1
            count += 1

            dirpathIn = dirpath
            dirpathOut = dirpathIn.replace('source', 'out')

            filenameIn = dirpathIn + "\\" + filename
            filenameOut = dirpathOut + "\\" + filename

            if path.exists(filenameOut):
                continue

            if not path.exists(dirpathOut):
                makedirs(dirpathOut)

            print(count, '\t', currentKey, '\t', filenameIn, '\t\t', filenameOut)

            tinify.key = keys[currentKey]
            source = tinify.from_file(filenameIn)
            source.to_file(filenameOut)

