import json
import os
from datetime import datetime

DATA_FILE = "data/checkins.json"


def initialize_memory():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


def save_checkin(mood, note):

    initialize_memory()

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    data.append(
        {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "mood": mood,
            "note": note
        }
    )

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_checkins():

    initialize_memory()

    with open(DATA_FILE, "r") as f:
        return json.load(f)
