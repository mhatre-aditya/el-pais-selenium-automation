USERNAME = "adityamhatre_cI2YZC"
ACCESS_KEY = "bC3pxhozDM2VdPiZpcUZ"


BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

browsers = [

{
    "browserName": "Chrome",
    "browserVersion": "latest",
    "bstack:options": {
        "os": "Windows",
        "osVersion": "11",
        "projectName": "ElPais Automation",
        "buildName": "Parallel Test",
        "sessionName": "Chrome Test"
    }
},

{
    "browserName": "Firefox",
    "browserVersion": "latest",
    "bstack:options": {
        "os": "Windows",
        "osVersion": "11",
        "projectName": "ElPais Automation",
        "buildName": "Parallel Test",
        "sessionName": "Firefox Test"
    }
},

{
    "browserName": "Edge",
    "browserVersion": "latest",
    "bstack:options": {
        "os": "Windows",
        "osVersion": "11",
        "projectName": "ElPais Automation",
        "buildName": "Parallel Test",
        "sessionName": "Edge Test"
    }
},

{
    "browserName": "Chrome",
    "browserVersion": "latest",
    "bstack:options": {
        "os": "OS X",
        "osVersion": "Monterey",
        "projectName": "ElPais Automation",
        "buildName": "Parallel Test",
        "sessionName": "Mac Chrome Test"
    }
},

{
    "browserName": "Safari",
    "bstack:options": {
        "deviceName": "iPhone 14",
        "realMobile": "true",
        "projectName": "ElPais Automation",
        "buildName": "Parallel Test",
        "sessionName": "iPhone Test"
    }
}

]