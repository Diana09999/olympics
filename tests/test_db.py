from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100
    assert len(db.get_countries(limit=1)) == 1


def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 100
    assert len(db.get_athletes(limit=1)) == 1


def test_disciplines():
    rows = db.get_disciplines()
    assert len(rows) > 40
    assert len(db.get_disciplines(limit=1)) == 1


def test_teams():
    rows = db.get_teams()
    assert len(rows) > 100
    assert len(db.get_teams(limit=1)) == 1


def test_events():
    rows = db.get_events()
    assert len(rows) > 100
    assert len(db.get_events(limit=1)) == 1


def test_medals():
    rows = db.get_medals()
    assert len(rows) > 100
    assert len(db.get_medals(limit=1)) == 1


def test_discipline_athletes():
    assert len(db.get_discipline_athletes(1)) >= 10


def test_top_countries():
    assert len(db.get_top_countries()) >= 10


def test_collective_medals():
    assert len(db.get_collective_medals()) >= 10


def test_top_collective():
    assert len(db.get_top_collective()) >= 10


def test_individual_medals():
    assert len(db.get_individual_medals()) >= 10
    assert len(db.get_individual_medals(limit=1)) == 1


def test_top_individual():
    assert len(db.get_top_individual()) >= 10
