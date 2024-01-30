from app.structures import CVData

cv_data: CVData = {
    "personal": {
        "name": "Andrei Tiltu",
        "email": "andreitiltu@gmail.com",
        "phone": "+37361041232",
        "position": "Backend developer",
    },
    "experience": [
        {
            "title": "Backend Developer",
            "company": "Power IT",
            "location": "Chisinau, Moldova",
        },
        {
            "title": "Fullstack developer",
            "company": "YMK-IT management",
            "location": "Balti, Moldova"
        },
    ],
    "education": [
        {
            "degree": "Computer science (programming)",
            "school": "Alecu Russo State University of Bălți",
            "location": "Balti, Moldova",
            "graduation_date": "May 2022",
        }
    ],
    "languages": [
        {
            "name": "Romanian",
            "understanding": "Native",
            "speaking": "Native",
            'writing': "Native"
        },
        {
            "name": "Russian",
            "understanding": "Native",
            "speaking": "Native",
            'writing': "Native"
        },
        {
            "name": "English",
            "understanding": "Advanced",
            "speaking": "Medium",
            'writing': "Advanced"
        },
    ]
}
