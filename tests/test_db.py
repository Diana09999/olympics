from olympics import db


def test_get_athletes(id=None):
    rows = db.get_athletes(500)
    assert len(rows) > 100


def test_get_countries():
    rows = db.get_countries(100)
    assert len(rows) == 1


def test_get_connection():
    rows = db.get_connections(20)
    assert len(rows) > 10


def test_get_disciplines(id=None):
    rows = db.get_discipilines(6000)
    assert len(rows) > 1


def test_get_teams(id=None):
    rows = db.get_teams(500)
    assert len(rows) > 100


def test_get_events(id=None):
    rows = db.get_events(85)
    assert len(rows) > 29


def test_get_medals(id=None):
    rows = db.get_medals(320)
    assert len(rows) > 100


def test_get_discipline_athletes(discipline_id):
    rows = db.get_discipline_athletes(3)
    assert len(rows) > 3


def test_get_top_countries(top=10):
    rows = db.get_top_countries(96)
    assert len(rows) > 47


def test_get_collective_medals(team_id=None):
    rows = db.get_collective_medals(3)
    assert len(rows) > 2


def test_get_top_collective(top=10):
    rows = db.get_top_collective(1000)
    assert len(rows) > 10


def test_get_individual_medals(athlete_id=None):
    rows = db.get_individual_medals(20)
    assert len(rows) > 15


def test_get_top_individual(top=10):
    rows = db.get_top_individual(100)
    assert len(rows) == 100


def test_get_select_country():
    rows = db.get_countries(70)
    assert len(rows) == 1
