import json

import pytest

from admission_fee import app

def test_is_admission_fee():
    assert app.is_admission_fee(3) == 1800


