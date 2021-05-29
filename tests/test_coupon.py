import pytest

from unittest.mock import patch

from wayfair.tests.conftest import (
    COUPONS,
    CATEGORY_NO_RESULTS,
    CATEGORY_ONE_RESULT,
    CATEGORY_MULTIPLE_RESULTS,
)
from wayfair.app import Coupon


@pytest.mark.parametrize(
    "category_data, expected_result",
    [
        (CATEGORY_NO_RESULTS, 0),
        (CATEGORY_ONE_RESULT, 1),
        (CATEGORY_MULTIPLE_RESULTS, 2),
    ],
)
@patch("wayfair.app.Coupon.get_coupon_data")
def test_get_coupons_for_category(coupon_mock, category_data, expected_result):
    """
    Test category/coupon find for no result, one result and multiple results
    """
    coupon_mock.return_value = COUPONS
    coupon_obj = Coupon()
    coupons = coupon_obj.get_coupons_for_category(category_data[0]["category_name"])

    assert type(coupons) is list
    assert len(coupons) == expected_result
    assert coupon_mock.called


def test_can_get_coupon_data():
    """
    Test we can get coupon data
    """
    coupon_obj = Coupon()
    coupons = coupon_obj.get_coupon_data()
    assert type(coupons) is list
    assert len(coupons) > 1


def test_sort_coupons_by_date_field_most_recent():
    """
    Test that we get coupons sorted by most recent date.
    """
    coupon_obj = Coupon()
    sorted_coupons = coupon_obj.sort_coupons_by_date_field(
        COUPONS, "date_modified", True
    )

    assert sorted_coupons[0] == "coupon_3"
    assert sorted_coupons[1] == "coupon_2"
    assert sorted_coupons[2] == "coupon_1"


def test_sort_coupons_by_date_field_oldest_first():
    """
    Test that we get coupons sorted by oldest first.
    """
    coupon_obj = Coupon()
    sorted_coupons = coupon_obj.sort_coupons_by_date_field(
        COUPONS, "date_modified", False
    )

    assert sorted_coupons[0] == "coupon_1"
    assert sorted_coupons[1] == "coupon_2"
    assert sorted_coupons[2] == "coupon_3"
