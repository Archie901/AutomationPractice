import random

class Requests:    
    dev_api_domain = "https://api-dev.trueqrcode.com"
    prod_api_domain = "https://api.trueqrcode.com"
    dev_url_domain = "https://dev.trueqrcode.com"   
    path_login = "/api/v1/public/auth/sign-in"
    path_profile = "/api/v1/private/auth/me"
    path_tempCreate ="/api/v1/private/qr-template"
    path_qrCreate = "/api/v1/private/qr-code"    
    path_qrSingle = "/api/v1/private/qr-code/"
    path_scan = "/api/v1/public/scans/"
    headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive"}
    access_token = None

class Customers:
    dev_customerCreds = (
        ["komic@mailinator.com", "Something555!"],
        ["mykemos@protonmail.com", "Qwerty2233!"],
        ["merkar@mailinator.com", "Something555!"],
        ["porterbird12@gmail.com", "Qwerty123!"],
        ["zovid@mailinator.com", "Qwerty123!"],
        ["someid@mailinator.com", "Qwerty123!"],
        ["fahaw@mailinator.com", "Qwerty123!"],
    )
    prod_customerCreds = ["mykemos@protonmail.com", "Something555!"]

    def randomCreds():
        randomCreds= random.choice(Customers.dev_customerCreds)
        return randomCreds

class Scans:
    deviceIds = ["8c115a70-4d48-4f47-8245-86ffaffe5d16","2552d0b2-ecfc-4cf1-8378-58646860014c","0f93dd8b-7530-40bc-af78-d3ea5cba77d7",
                 "42209e25-daab-4d2e-9a07-7e27eba4076b","4cccc522-c895-4050-becf-a9d652835f4c","fa641144-9ee9-4258-861d-f5508b03cdf5",
                 "e7d699f3-fdc8-4bad-8385-5ac6007d4f9d","47aee305-ee67-4140-a719-e43602ed3d7c","52b694d1-824d-4dd9-96c7-8971ef822727",
                 "9cb1e2f8-3838-4c10-a9fd-04aa4c5928a7","5d3e90cc-6bbf-4ed7-9eef-ba0fa90fb85c","5303374c-a893-4979-a444-6e12167c7d25",
                 "fb616704-34a0-488b-9dc4-e47d31d1d498","ff61d0b4-105b-4757-9da9-c9c8d81a46c0","f99f6959-55c6-4e6b-8f88-739d59aaba0d",
                 "0626aee7-e1d4-43b3-91a1-2f9275cab258","d449624c-930a-4cc0-bac7-81bd215e49fe","5fde1645-79b5-4ed1-89c7-6f5b545dd6a0",
                 "f0357f62-5144-4fbb-b9ca-5c902fd75379","a470d86f-253c-4ec7-831e-8a146c88be36"]
    AfricaLats = [18.7932, 14.4235, 12.0094, 9.9443, 4.1331, -1.4546, -5.8998, -9.0554, -13.9544, -17.8323]
    AfricaLngs = [13.6554, 17.0324, 20.1111, 22.4543, 25.6325, 27.0000, 30.7454, 32.6666, 34.2222, 36.1000]
    AsiaLats = [40.8600, 37.7775, 35.0015, 33.7532, 31.8574, 28.7743, 26.3444, 26.0000, 24.5352, 22.8383]
    AsiaLngs = [75.1111, 78.0326, 82.0034, 88.6666, 93.4231, 97.0000, 104.8831, 109.5545, 113.0909, 116.0013]
    NorthAmerLats = [53.2333, 51.0909, 49.1321, 47.6666, 45.0001, 43.6214, 41.7713, 39.3287, 37.0745, 35.5555]
    NorthAmerLngs = [-120.2565, -117.1111, -113.0000, -108.0909, -104.6753, -99.3215, -97.8843, -93.1346, -88.5555, -82.0041]
    SouthAmerLats = [-18.9545, -16.9000, -14.8111, -12.7454, -10.7312, -8.6910, -6.6700, -4.6000, -2.5733, -1.5098]
    SouthAmerLngs = [-71.0011, -67.8871, -64.0000, -62.9898, -58.6531, -55.4445, -53.0081, -51.3333, -49.87233, -46.0303]
    EuropeLats = [45.5199, 46.0981, 47.2223, 47.7623, 48.1344, 49.5555, 50.8888, 51.5321, 52.0000, 52.7611]
    EuropeLngs = [5.5111, 7.7713, 10.8122, 13.7432, 17.0065, 19.7195, 22.0003, 24.0000, 27.8653, 29.0003]
    UkraineLats = [50.4101, 48.3794, 49.1223, 51.2146, 50.0004, 48.0266, 51.0909]
    UkraineLngs = [30.5303, 25.9813, 32.8711, 31.9090, 26.7777, 28.7545, 26.9876]

    #dev_qrIds = ["E5F1ADAM","SZGK843B","NPYDMDX3"]
    #Komic codes

    dev_qrIds = ["VFRRH3BR","JJZXVUZD","LLD9U6YD"]
    #Mykemo codes

    prod_qrIds = ["CZNR1FS1","3ZHPT5K8"]
    #Mykemo codes
    
    def randomDeviceId():
        randomDeviceId= random.choice(Scans.deviceIds)
        return randomDeviceId
    def randomLat():
        randomLat= random.choice(Scans.NorthAmerLats)
        return randomLat
    def randomLng():
        randomLng= random.choice(Scans.NorthAmerLngs)
        return randomLng
    def dev_randomQRid():
        dev_randomQRid= random.choice(Scans.dev_qrIds)
        return dev_randomQRid
    def prod_randomQRid():
        prod_randomQRid= random.choice(Scans.prod_qrIds)
        return prod_randomQRid
    
class QRcodes_Templates:
    TemplateNames = ["Reprehe", "ErroCequAtur", "atibu_modi_fam", "!!Croieemus!!"]
    QRnames = ["Let me see!", "sTranGe ThiNGs", "123__333__888", "make them still", "<<NOTHING LEFT!>>", "QRcode, it's ok", "MAY i Serve?"]
    frameTexts = ["JUST DO IT", "COMING IS NOW", "ANGER TO GO", "$%!@))*", "_11124_", "Scan Smth", "$$$$", "ALOT"]
    backgroundColors = ["#cde99f", "#ffffff", "#a7e0d4", "#eec0ae"]
    patternColors = ["#e20c0ca8", "#804801", "#000000", "#026924", "#9104ad"]
    cornerColors = ["#008327a8", "#010e80", "#4e4e4e", "#000000", "#e60f08"]
    frameTypes = ["NONE", "NO_BORDER", "BORDER", "BORDER_INTERRUPTION", "BORDER_SPACE_LABEL_TOP"]
    patternTypes = ["SQUARE", "CLASSY", "CLASSY_ROUNDED", "DOTS", "EXTRA_ROUNDED", "ROUNDED"]
    cornerTypes = ["SQUARE", "FULL_CIRCLE", "ROUNDED"]
    targetURLs = ["https://www.englishgrammar.org", "https://wordcounter.net/character-count", "https://advice.writing.utoronto.ca",
                  "https://whatismyipaddress.com", "https://pairwise.yuuniworks.com", "https://uxdesign.cc", "https://www.altexsoft.com"]
    library_ids = ['ae6eadae-e652-474c-af45-8cf4697c23df','5c91fb32-749d-435b-a7e5-80ea9ba5b78a', 'b69be0da-a5a3-4934-aedd-c9cb43cf94b5',
                   '56109ab1-26d5-4ff3-9821-8a76f93ea099','7bb1186b-44df-4d64-ad8e-fd89eb72b106', '13bd9c18-dfbd-466f-bdba-8a3dc7189dbb',
                   '3ac3f020-5293-4ea5-b528-b05209963e2a','e7909b33-9ae9-407c-84a9-d454971580ea', '14d8d2aa-456f-4b3a-ad74-a765d1dc2992',
                   '62d5386e-b04f-4889-b7b5-8dce7a2a4034','6de257c8-e208-4156-9af6-f02db2f765c2', None]
    
    def randomTemplateName():
        randomTemplateName = random.choice(QRcodes_Templates.TemplateNames)
        return randomTemplateName    
    def randomQRname():
        randomQRname = random.choice(QRcodes_Templates.QRnames)
        return randomQRname
    def randomFrameText():
        randomFrameText = random.choice(QRcodes_Templates.frameTexts)
        return randomFrameText
    def randomBackColor():
        randomBackColor = random.choice(QRcodes_Templates.backgroundColors)
        return randomBackColor
    def randomPatternColor():
        randomPatterColor = random.choice(QRcodes_Templates.patternColors)
        return randomPatterColor
    def randomCornerColor():
        randomCornerColor= random.choice(QRcodes_Templates.cornerColors)
        return randomCornerColor
    def randomFrameType():
        randomFrameType= random.choice(QRcodes_Templates.frameTypes)
        return randomFrameType
    def randomPatternType():
        randomPatternType= random.choice(QRcodes_Templates.patternTypes)
        return randomPatternType
    def randomCornerType():
        randomCornerType= random.choice(QRcodes_Templates.cornerTypes)
        return randomCornerType
    def randomTargetUrl():
        randomTargetUrl= random.choice(QRcodes_Templates.targetURLs)
        return randomTargetUrl
    def randomLibraryId():
        randomLibraryId= random.choice(QRcodes_Templates.library_ids)
        return randomLibraryId