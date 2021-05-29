import pytest

CATEGORY_NO_RESULTS = [
    {"category_name": "no stuff", "category_parent_name": "no parent stuff"},
]

CATEGORY_ONE_RESULT = [
    {"category_name": "one thing", "category_parent_name": "one parent thing"},
]

CATEGORY_MULTIPLE_RESULTS = [
    {"category_name": "multi thing", "category_parent_name": "multi parent thing"},
]

COUPONS = [
    {
        "category_name": "one thing",
        "coupon_name": "coupon_1",
        "date_modified": "2019-01-01",
    },
    {
        "category_name": "multi thing",
        "coupon_name": "coupon_2",
        "date_modified": "2020-01-01",
    },
    {
        "category_name": "multi thing",
        "coupon_name": "coupon_3",
        "date_modified": "2021-01-01",
    },
]
