import pytest

from wayfair.model import CategoryModel, CouponModel


def test_category_model():
    """
    Test that we have can query for category data and all relevant fields exist.
    """
    category_data = CategoryModel().get_category_data()

    assert type(category_data) is list
    assert len(category_data) > 1
    for data in category_data:
        assert "category_name" in data
        assert "category_parent_name" in data


def test_coupon_model():
    """
    Test that we have can query for coupon data and all relevant fields exist.
    """
    coupon_data = CouponModel().get_coupon_data()

    assert type(coupon_data) is list
    assert len(coupon_data) > 1
    for data in coupon_data:
        assert "category_name" in data
        assert "coupon_name" in data
        assert "date_modified" in data
