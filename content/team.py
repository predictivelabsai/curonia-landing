"""People shown on the Curonia Capital site.

To add someone, append a dict. Only "name" and "initials" are required.
- photo: file name in static/team/ (portrait, about 800 x 910 px, JPG or WebP).
  Photos are shown in black and white; until one is added a monogram is shown.
- role_key: translation key in utils/i18n.py for the job title.
- bio_key: translation key for a short biography (shown under "Profile").
- email, phone: shown only when provided. Use international phone format.
"""

TEAM = [
    {
        "name": "Julian Kaljuvee",
        "initials": "JK",
        "photo": None,
        "role_key": None,
        "bio_key": "julian_bio",
        "email": None,
        "phone": None,
        "linkedin": "https://www.linkedin.com/in/juliankaljuvee/",
    },
    {
        "name": "Igors Plahins",
        "initials": "IP",
        "photo": None,
        "role_key": None,
        "bio_key": "igors_bio",
        "email": None,
        "phone": None,
        "linkedin": "https://www.linkedin.com/in/igorplahin/",
    },
]
