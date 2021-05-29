import pytest

from ..app import Category


def test_category_has_access_to_model_data():
    """
    Test that get_category_data has access to Category model data
    """
    category = Category()
    category_data = category.get_category_data()

    assert type(category_data) is list
    assert len(category_data) > 1
