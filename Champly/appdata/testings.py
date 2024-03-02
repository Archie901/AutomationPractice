import random

class Methods:
    def randomizer(x):
        randomed = random.choice(x)
        return randomed

class Requests:
    org_id = 30
    stage_api_domain = "https://staging-api.champly.io"
    path_login = "/api/login"
    path_users = f"/api/organizations/{org_id}/users"
    path_sites = f"/api/organizations/{org_id}/sites"
    headers = {"Content-Type": "application/json",
               "Accept-Encoding": "charset=utf-8",
               "Connection": "keep-alive"}

class Creds:
    stage_superCreds = (
        ["supervi@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"]
    )
    stage_adminCreds = (
        ["adminus@maildrop.cc", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"],
        ["ryde@maildrop.cc", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"]
    )
    stage_managerCreds = (
        ["managerus1@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"],
        ["managerus2@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"]
    )
    stage_memberCreds = (
        ["memberik1@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"],
        ["memberik2@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"],
        ["memberik3@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"],
        ["memberik4@mailinator.com", "Asdfghjkl1234567890poiuytrewqmnbvcxz!"]
    ) 

class General:
    emails1 = ["joglo@me.com", "bradl@verizon.net", "jdhedden@yahoo.ca", "smallpaul@gmail.com", "staffelb@optonline.net", "damian@att.net",
              "grolschie@yahoo.com", "mcsporran@me.com", "andersbr@att.net", "mstrout@outlook.com", "penna@yahoo.ca", "fallorn@optonline.net",
              "kdurhwzo35@mail.com", "ukkovfyi58@mail.com", "qyekincx67@aol.com", "aizsumqx38@hotmail.com", "qmuujxox78@yahoo.com", "gihwluza54@aol.com",
              "xtushxwl51@yahoo.com", "fdkcaufe44@hotmail.com", "dqvdclkc10@gmail.com", "bvzkzirv26@outlook.com", "szjpuati57@aol.com", "hlpdlrwc15@yahoo.com",
              "hkajlbpq68@gmail.com", "fnuygbvl68@outlook.com", "qaknblke47@yahoo.com", "gqqjgnul22@gmail.com", "eeggzbmc27@yahoo.com",
              "jsmlesjs97@hotmail.com", "fdvxyneu25@yahoo.com", "krenafzn28@mail.com"]
    emails2 = ["gzcgttcr66@aol.com", "kkdeklow60@outlook.com", "fvriruoe2@outlook.com", "yvzoxciz61@mail.com", "icnjqmve18@mail.com", "nvxqtmrw70@aol.com",
               "bcifmdta58@outlook.com", "dwaodvkv76@yahoo.com", "ptvarscc20@hotmail.com", "osjlvqun16@gmail.com", "gppwtcxl65@mail.com", "iwlrioio77@hotmail.com",
               "jlysmlvk84@yahoo.com", "iliezlxr40@hotmail.com", "gqsyhpvr51@hotmail.com", "ijfulush32@aol.com", "epurgdgv59@aol.com", "nqkmpfae45@yahoo.com",
               "axeftgex19@aol.com", "pobvbvfo42@outlook.com"]
    firstNames =["Aditya", "Kaila", "Maribel", "Jaylen", "Christian", "Ernest", "Regan", "Valentino", "Lilianna", "Zaiden", "Iris", "Jaida", "Grego",
                 "Monty", "Manicolo", "Manolo", "Urgens", "Biov", "Bobic", "Qwerty", "Master", "Circa", "Zackus", "Antoinette", "Smith", "Vega", "Spencer",
                 "Tami", "Lewis", "Jamie", "Willie", "Harold", "Tommy", "13123", "Qwerty123!"]
    lastNames = ["Sharp", "Guerrero", "Trevino", "Rosario", "Montoya", "Schneider", "Gates", "Middleton", "Austin", "Rowland", "Andrews", "Holloway",
                 "Midrac", "Tokerv", "Tmatchenko", "Bordov", "Ignasios", "Stemplatten", "Skorovodov", "Nutrkio", "Ibragimus", "Phelps", "Sherri",
                 "Veraluz", "Fox-fox", "Harmon", "Gerardo", "Cohen", "Russell", "Snyder", "Wilkerson", "90090", "Asdfgh345?"]
    titles = ["Provider of goods", "Senior assistant of helper", "Best employee eva", "A man with issues", "Workers of workers", "Supplier of things",
              "Just a useful person", "Fine maker", "A identity to consider", "Normalizer", "Leader of great people", "Not a boss", "Laborolog", "9594069",
              "+=1-30213=+", "<<<234>>>", "Qwerty123!", "/;'423n/./", "Asdfgh345?"]
    phrases = ["Roll With the Punches", "Give a Man a Fish", "Fool's Gold", "A Dog in the Manger", "Two Down, One to Go", "No Ifs, Ands, or Buts",
               "Back To the Drawing Board", "Swinging For the Fences", "Burst Your Bubble", "Short End of the Stick", "Know the Ropes", "83663663"]
    companies = ["Wild West Outreach", "Asap Marketing 2", "Partners and thing LTD", "Wind Eagle Marketing", "Haq Technologies", "Take Touchdown",
                 "Atomic Army Surplus", "Berco Architects inc.", "Wilson & Kinsey LTD", "Kota Art Works", "Advanced Black Spot", "013125"]
    weblinks = ["https://www.englishgrammar.org", "https://wordcounter.net/character-count", "https://advice.writing.utoronto.ca",
                  "https://whatismyipaddress.com", "https://pairwise.yuuniworks.com", "https://uxdesign.cc", "https://www.altexsoft.com",
                  "https://stripe.com/docs/testing", "https://www.freeimageslive.co.uk", "https://dummyimage.com", "https://www.charactercountonline.com",
                  "https://learnenglish.britishcouncil.org", "https://qatechnicals.wordpress.com", "https://twitter.com", "https://www.tiktok.com/en",
                  "https://testsigma.com/blog/test-cases-example-for-web-application/", "https://www.guru99.com/complete-web-application-testing-checklist.html",
                  "https://onlinetestcase.com/test-cases-for-testing-website/", "http://www.testingmcafeesites.com/testcat_be.html", "http://example.com/"]