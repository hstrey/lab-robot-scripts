import string

    def translateWell(wellName):
        wellList=list(wellName)
        if len(wellList) ==2:
            lower(wellList[0])=letter
            wellList[1]=j
        elif len(wellList) ==3:
            lower(wellList[0])=letter
            j=wellList[1]+wellList[2]
        values=dict()
        for index, letter in enumerate(string.ascii_lowercase):
            values[letter] = index + 1
            