import random

class Requests:    
    dev_api_domain = "https://api-dev.trueqrcode.com"
    prod_api_domain = "https://api.trueqrcode.com"
    dev_url_domain = "https://dev.trueqrcode.com"   
    path_login = "/api/v1/public/auth/sign-in"
    path_scan = "/api/v1/public/scans/"
    path_qrCreate = "/api/v1/private/qr-code"    
    headers = {"Content-Type": "application/json", "Accept-Encoding": "charset=utf-8", "Connection": "keep-alive"}

class Customers:
    dev_customerCreds = (
        ["komic@mailinator.com", "Something555!"],
        ["mykemos@protonmail.com", "Qwerty2233!"],
        ["merkar@mailinator.com", "Something555!"]
    )
    prod_customerCreds = ["mykemos@protonmail.com", "Something555!"]

class Scans:
    deviceIds = ["8c115a70-4d48-4f47-8245-86ffaffe5d16","2552d0b2-ecfc-4cf1-8378-58646860014c","0f93dd8b-7530-40bc-af78-d3ea5cba77d7","42209e25-daab-4d2e-9a07-7e27eba4076b",
            "4cccc522-c895-4050-becf-a9d652835f4c","fa641144-9ee9-4258-861d-f5508b03cdf5","e7d699f3-fdc8-4bad-8385-5ac6007d4f9d","47aee305-ee67-4140-a719-e43602ed3d7c",
            "52b694d1-824d-4dd9-96c7-8971ef822727","9cb1e2f8-3838-4c10-a9fd-04aa4c5928a7","5d3e90cc-6bbf-4ed7-9eef-ba0fa90fb85c","5303374c-a893-4979-a444-6e12167c7d25",
            "fb616704-34a0-488b-9dc4-e47d31d1d498","ff61d0b4-105b-4757-9da9-c9c8d81a46c0","f99f6959-55c6-4e6b-8f88-739d59aaba0d","0626aee7-e1d4-43b3-91a1-2f9275cab258",
            "d449624c-930a-4cc0-bac7-81bd215e49fe","5fde1645-79b5-4ed1-89c7-6f5b545dd6a0","f0357f62-5144-4fbb-b9ca-5c902fd75379","a470d86f-253c-4ec7-831e-8a146c88be36"]
    latitudes = [50.4101, 51.6998, 46.4075, 42.0003, 52.8823, 40.6473, 42.6824, 32.3985, 33.1375, 65.2934]
    # additional latitudes which are not typical -32.2499, -20.9614, 23.7252
    longitudes = [30.5303, 22.1318, 24.1318, 21.1015, 20.7500, 23.4462, 29.6718, 27.9492, 31.8813, 28.1299]
    # additional longitudes which are not typical 02.9882, 12.7441, 17.4462, -33.5820, -33.5820, -104.2382, -100.8984, -64.3359
    UkraineLats = [50.4101, 48.3794, 49.1223, 51.2146, 50.0004, 48.0266, 51.0909]
    UkraineLngs = [30.5303, 25.9813, 32.8711, 31.9090, 26.7777, 28.7545, 26.9876]
    dev_qrIds = ["5X5TAGX3", "RE7A9F26", "UHM7T997"]
    prod_qrIds = ["CZNR1FS1","3ZHPT5K8"]

class QRcodes:
    QRnames = ["Let me see!", "sTranGe ThiNGs", "123__333__888"]
    frameTexts = ["JUST DO IT", "COMING IS NOW","ANGER TO GO"]
    patternColors = ["#64014b", "#97631e", "#066e97"]
    frameTypes = ["BORDER", "BORDER_INTERRUPTION", "NO_BORDER"]
    patternTypes = ["SQUARE", "CLASSY_ROUNDED", "EXTRA_ROUNDED"]
    cornerTypes = ["SQUARE", "FULL_CIRCLE", "ROUNDED"]
    targetURLs = ["https://www.englishgrammar.org", "https://wordcounter.net/character-count", "https://advice.writing.utoronto.ca"]

class Functions:
    def randomizer(x):
        return random.choice(x)