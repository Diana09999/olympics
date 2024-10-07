from olympics import db


def get_athletes(id=None):
    rows = db.get_athletes()
    assert len(rows) > 100


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 69


def get_connection():
    rows = db.get_connecetions()
    assert len(rows) > 50


def get_disciplines(id=None):
    rows = db.get_discipilines()
    assert len(rows) > 1


def get_teams(id=None):
    rows = db.get_teams()
    assert len(rows) > 100


def get_events(id=None):
    rows = db.get_events()
    assert len(rows) > 85


def get_medals(id=None):
    rows = db.get_medals()
    assert len(rows) > 100


def get_discipline_athletes(discipline_id):
    rows = db.get_discipline_athletes()
    assert len(rows) > 20


def get_top_countries(top=10):
    rows = db.get_top_countries()
    assert len(rows) > 96


def get_collective_medals(team_id=None):
    rows = db.get_collective_medals()
    assert len(rows) > 3


def get_top_collective(top=10):
    rows = db.get_top_collective()
    assert len(rows) > 10


def get_individual_medals(athlete_id=None):
    rows = db.get_individual_medals()
    assert len(rows) > 15


def get_top_individual(top=10):
    rows = db.get_top_individual()
    assert len(rows) > 100
