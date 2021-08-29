from wsa.functions import refactor, add
import pytest
import pandas as pd
import os

test_path = os.getcwd() + "/tests"


def test_refactor():
    t_file = pd.read_excel(f"{test_path}/test_assets/t-file.xlsx")
    input_df = refactor(t_file)

    assert isinstance(input_df, list) == True
