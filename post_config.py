from datetime import datetime

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def format_date(t: datetime):
    return f"{t.day}{suffix(t.day)} {t.strftime('%B, %Y')}"

POSTS = [
    {
        "title": "The Prophecy of Nihit",
        "date": datetime(2023, 4, 12),
        "filename": "1.png",
        "description": "By divine guidance, our dear <span style='color: brown;'>Bund Baba</span> and <span style='color: orange;'>\
            Kinna</span> have foretold the conversion to Nihit to his true Trans nature by 2027. <span style='color: cyan'>@Nihit</span>\
                  dw, we support you in your every decision."
    },
    {
        "title": "We Support Farmers",
        "date": datetime(2023, 4, 11),
        "filename": "4.jpg",
        "description": "Just an ordinary photo of our villager doing normal things."
    },
    {
        "title": "The Kopcha Assembles",
        "date": datetime(2022, 11, 14),
        "filename": "2.jpg",
        "description": "Just don't ask why we were leaning like that."
    },
    {
        "title": "#BadassBUNDkumar",
        "date": datetime(2022, 11, 14),
        "filename": "3.jpg",
        "description": "The title and picture say enough"
    },
    {
        "title": "Choo... CHOO....",
        "date": datetime(2022, 11, 14),
        "filename": "6.jpg",
        "description": "There's absolutely no such thing as being too-high....."
    },
    {
        "title": "#NihitApproves",
        "date": datetime(2022, 10, 28),
        "filename": "5.jpg",
        "description": "Whatever it may be, You have consent and approval from Nihit now."
    },
]