```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from main import app, receive_github_event

@pytest.fixture
def mock_request():
    mock = MagicMock()
    mock.json = AsyncMock(return_value={
        "commits": [
            {
                "id": "commit_sha_1",
                "modified": ["file1.py"]
            },
            {
                "id": "commit_sha_2",
                "modified": ["file2.js"]
            }
        ],
        "repository": {
            "full_name": "username/repo"
        }
    })
    return mock

def test_receive_github_event_no_commits(mock_request):
    result = app.asgi(mock_request).post("/webhook")
    assert result == {"status": "No commits found in the payload."}

@patch("main.get_file_content")
@patch("main.generate_unit_test")
@patch("main.open")
def test_receive_github_event_with_commits(mock_open, mock_generate_unit_test, mock_get_file_content, mock_request):
    mock_get_file_content.return_value = "def add(a, b):\n    return a + b"
    mock_generate_unit_test.return_value = "def test_add():\n    assert add(1, 2) == 3"

    result = app.asgi(mock_request).post("/webhook")

    assert result == {"status": "Tests generated and executed"}
    mock_open.assert_called()
```