from enum import Flag
from wsa.functions import Messager
import pytest
import pandas as pd
import os


test_path = os.getcwd() + "/tests"


def test_refactor():
    t_msg = Messager()
    t_file = pd.read_excel(f"{test_path}/test_assets/t-file.xlsx")
    input_df = t_msg.refactor(t_file)

    assert isinstance(input_df, list) == True


@pytest.mark.parametrize("sample, is_ok", [("hello", True), (123, False)])
def test_validate(sample, is_ok):
    t_msg = Messager()
    assert t_msg.validate(sample) == is_ok
