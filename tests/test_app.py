import pytest

from unittest.mock import patch

from wayfair.app import App


@patch("builtins.print")
def test_get_coupons_for_all_categories(print_mock):
    """
    Test we can run the application and get results.
    """
    app_obj = App()
    app_obj.get_coupons_for_all_categories()

    assert print_mock.called
    print_mock.assert_called_with("Category Name = Baby And Kids => []")
