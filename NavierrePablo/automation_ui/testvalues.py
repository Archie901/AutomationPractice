import random

class Methods:

    def randomizer(x):
        randomed = random.choice(x)
        return randomed

class Requests:

    devstage_pablo_url_domain = "https://pablo-dev.vercel.app"
    prod_pablo_url_domain = "https://www.navierre.com"
    dev_pablo_domain = "https://api-synergyhealth-dev.osdb.io"
    stage_pablo_domain = "https://api-synergyhealth-stage.osdb.io"
    headers = {"Content-Type": "application/json",
               "Accept-Encoding": "charset=utf-8",
               "Connection": "keep-alive"}

class General:
    
    practice_search = ("Medical Lab", "Clinical Facility", "Rehab Center", "Great Place", "Pharmacy", "Store Goods", "Best Shelter")

    diff_values = ("123_structure_009", "-protect-55!", "way of examination", "[097513213]", "random_things_showed", "exhibition_neck",
                   "devoteToLook", "((industrials123))", "!!banish_money]}", "<<hardware_autonomy>>", "top drawer??", "fraudSSSport", "HH-8076-AA",
                   "AA-0909-BC", "77-guys-334", ">?>?>feeling", "{tedious234", "vacuous", "normal", ":::passenger:::", "license", "broad", "traumatize",
                   "sentinent", "(.<Ruler>.)", "??Trapping??", ",,Summerthing91!", "temper,,", "chieftain", "recondite", "Romantic", "Rhetorical")
    
    emails = ("dofuqo@mailinator.com", "wydex@mailinator.com", "morsoko@mailinator.com", "autotesting@mailinator.com", "radomik@mailinator.com",
              "qwertuq@mailinator.com", "ximatoz@mailinator.com", "josterko@mailinator.com", "loikolu@mailinator.com", "macdisk@mailinator.com",
              "poiko@mailinator.com", "dwarves@mailinator.com", "lapadit@mailinator.com", "rolans@mailinator.com", "dryfuse@mailinator.com",
              "iokler@mailinator.com", "qwertus@mailinator.com", "nioxes@mailinator.com", "zaribaydu@mailinator.com", "kutsenko@mailinator.com",
              "mordat@mailinator.com", "glaynich@mailinator.com", "fusteri@mailinator.com", "vivusik@mailinator.com")
    
    usPhoneNums = ("13156391271", "12067046212", "13152593482", "13152593484", "13152593485", "13152593481", "13152593478", "12035472089",
                  "12035472101", "12019058727", "14305416275", "14052955409", "16085617464", "12242864639", "14013214382", "17144856307",
                  "12148140654", "12818101867", "17632200857", "17372420880", "17146968342")
    
    firstNames = ("Allen","Baylor","Everett","Gerald","Griffin","Jamari","Kayson","Kenzo","Ronald","Thomas","Alianna","Aya","Eleanora",
                  "Elia","Halle","Jovie","Kamila","Mikayla","Rosalia","Scarlett")

    lastNames = ("Knapp","Evans","Aguirre","Frazier","Jenkins","Savage","Lucero","Atkins","Hogan","Ware","Cantu","Rogers","Fuentes",
                 "Frederick","Daniel","Pineda","Delacruz","Mullins","Reiders","Bakertin")
    
    datesOfBirth = ("09091990","11111911")