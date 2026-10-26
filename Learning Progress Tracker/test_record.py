import csv

from records import add_records,view_records

def test_add_records(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    inputs = iter([
        "2026-10-26",
        "Python File I/O",
        "1.5",
        "CS50P"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_records()

    with open("learning_records.csv", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    assert len(records) == 1
    assert records[0]["Date"] == "2026-10-26"
    assert records[0]["Topic"] == "Python File I/O"
    assert records[0]["Duration"] == "1.5"
    assert records[0]["Resource"] == "CS50P"

def test_view_records_file_not_found(
        tmp_path,
        monkeypatch,
        capsys
):
    monkeypatch.chdir(tmp_path)

    view_records()

    captured = capsys.readouterr()
    
    assert "File Not Found" in captured.out