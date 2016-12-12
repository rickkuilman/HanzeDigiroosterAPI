# Digirooster API 🎓

## What is it?
The Digirooster API is an unofficial api to get information of the Hanze University time schedules.

## Getting started
1. Install Python 3.x. During the installation keep the checkbox for "installing pip" checked
2. Install requests via pip: ``pip install requests``
3. Install cherrypy via pip: ``pip install cherrypy``
4. Copy (and paste) "env_EXAMPLE.py" and change the name of the copy to "env.py". Edit the content of env.py according to your credentials for the Hanze Intranet.
5. Run server.py via the commandline ``python server.py``

# Methods

## schools()
    GET http://127.0.0.1:8080/schools
    
---

### Abstract
Retrieves all the schools currently available in the digirooster

### Response

| Name | Description |
|-----:|:-------------|
| **LongName** | Contains the name of the school |
| **ShortName** | Contains the letter code of the school (3 or 4 letter code) |
| **ID** | Contains the `schoolId`, that can be used further on in the API |

### Example

#### Request

    GET /schools HTTP/1.1
    Host: 127.0.0.1:8080

#### Response

    [
      {
        "LongName": "Academie voor Architectuur, Bouwkunde & Civiele Techniek",
        "ShortName": "SABC",
        "ID": "F77859ED31A4449917C761E84E7208B2"
      },
      {
        "LongName": "Academie Minerva",
        "ShortName": "SABK",
        "ID": "F77859ED31A4449917C761E84E7208AA"
      },
      ...
    ]

## groups()
    GET http://127.0.0.1:8080/groups/_schoolId_/_studyYear_

---

### Abstract
Retrieves all the groups currently available in the digirooster, for a specific school and year

### Parameters

| Name | Description |
|-----:|:-------------|
| **schoolId** | Should contain the `schoolId` of the group. Can be retrieved via `getSchools()` |
| **studyYear** | Should contain the year of the group: (1-4) |

### Response

| Name | Description |
|-----:|:-------------|
| `resourceId` | Contains the (short) name of the group |

### Example

#### Request

    GET /groups/F77859ED31A4449917C761E84E720894/4 HTTP/1.1
    Host: 127.0.0.1:8080

#### Response

    {
        "48E0614F807625FDF612ED87670FB9E9": "BUDK",
        "99030BAD69623C854AA2CF1AB103A3D3": "BUD4A",
        "2928A60834C6C958AF19F1C73019593F": "IBV4B",
        ...
    }

## schedule()
    GET http://127.0.0.1:8080/schedule/_resourceID_

---

### Abstract
Retrieves the current timetable of a group (resource)

### Parameters

| Name | Description |
|-----:|:-------------|
| **resourceID** | Should contain the `resourceID` of the group. Can be retrieved via `getGroups()` |

### Response

| Name | Description | |
|-----:|:-------------|:-- |
| `ScheduleId` | Contains the id of this schedule | |
| `ScheduleStart` | Contains a Unix timestamp with the starting date of this schedule | |
| `ScheduleEnd` | Contains a Unix timestamp with the ending date of this schedule | |
| `WeekData` | Contains a dict with data of the weeks: | |
| | `WeekStart` | Unix timestamp |
| | `WeekEnd` | Unix timestamp |
| |  `WeekNumber` | int |
| `ActivityData` | Contains a dict with the activities: | |
| | `Staff` | `String`, representing teacher |
| | `Location` | `String`, representing location |
| | `Left` | `int`, unknown property |
| | `ID` | `int`, representing id |
| | `Student` | `String`, representing the name of the group(s) taking this class |
| | `Description` | `String` |
| | `Start` | `Unix timestamp`, representing starting time of activity | 
| | `End` | `Unix timestamp`, representing ending time of activity |
| | `Width` | `int`, unknown property |
| | `Week` | `int`, representing weeknumber |

### Example

#### Request

    GET /schedule/99030BAD69623C854AA2CF1AB103A3C1 HTTP/1.1
    Host: 127.0.0.1:8080

#### Response

    {
      "ScheduleEnd": 1454686200000,
      "ChangeData": [],
      "ScheduleId": "99030BAD69623C854AA2CF1AB103A3D0",
      "ActivityData": [
        {
          "Staff": "NIEV",
          "Location": "EM/E143  C20",
          "Left": 0,
          "ID": "155689D466AB57A9D13D5E8E77744EAA",
          "Student": "BF\ITV4B",
          "Description": "T4.2 SE/practicum SA/SE",
          "End": 1447759800000,
          "Start": 1447752600000,
          "Width": 100,
          "Week": 47
        },
        ...
      "ScheduleStart": 1447666200000,
      "WeekData": [
        {
          "WeekEnd": 1448060399999,
          "WeekStart": 1447628400000,
          "WeekNumber": 47
        },
        ...
    }
    
## Disclaimer
This code is specifically for made for educational purposes (for IT students of the  Hanze University ), but I won't stop you from using it for a different purpose. I have no clue if you are allowed to use it, so you might want to contact the Hanze University if you're going to use it for something else.

Are you (an angry) legal counselor of the Hanze University? Please contact me through GitHub.

## Wanna help out?
Do you want to help make this code better or write a better readme? Clone the repo, check out to different branch (with a descriptive name) and create a pull request 👍
