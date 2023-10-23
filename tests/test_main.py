import json
from datetime import datetime
# Tests for the functions
import pytest
from datetime import datetime
from main import mask_account


def test_mask_account():
    assert mask_account("1234567890") == "**7890"
    assert mask_account("") == ""