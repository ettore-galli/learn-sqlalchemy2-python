from unittest.mock import MagicMock

from server.api.api import conteggio


def test_conteggio():
    mock_db = MagicMock()
    conteggio(db=mock_db)
    mock_db_calls = list(mock_db.mock_calls)
    assert str(mock_db_calls[0].args[0]) == "SELECT count(*) AS count_1 \nFROM invoice"
