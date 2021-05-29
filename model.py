from typing import List


class CouponModel:
    """
    Simulates a Coupon model that would return or persist data from a data store.
    """

    def get_coupon_data(self) -> List[dict]:
        return [
            {
                "category_name": "Comforter Sets",
                "coupon_name": "Comforters Sale",
                "date_modified": "2020-01-01",
            },
            {
                "category_name": "Comforter Sets",
                "coupon_name": "Cozy Comforter Coupon",
                "date_modified": "2020-01-01",
            },
            {
                "category_name": "Bedding",
                "coupon_name": "Best Bedding Bargains",
                "date_modified": "2019-01-01",
            },
            {
                "category_name": "Bedding",
                "coupon_name": "Savings on Bedding",
                "date_modified": "2019-01-01",
            },
            {
                "category_name": "Bed & Bath",
                "coupon_name": "Low price for Bed & Bath",
                "date_modified": "2018-01-01",
            },
            {
                "category_name": "Bed & Bath",
                "coupon_name": "Bed & Bath extravaganza",
                "date_modified": "2019-01-01",
            },
        ]


class CategoryModel:
    """
    Simulates a Category model that would return or persist data from a data store.
    """

    def get_category_data(self) -> List[dict]:
        return [
            {"category_name": "Comforter Sets", "category_parent_name": "Bedding"},
            {"category_name": "Bedding", "category_parent_name": "Bed & Bath"},
            {"category_name": "Bed & Bath", "category_parent_name": None},
            {
                "category_name": "Soap Dispensers",
                "category_parent_name": "Bathroom Accessories",
            },
            {
                "category_name": "Bathroom Accessories",
                "category_parent_name": "Bed & Bath",
            },
            {
                "category_name": "Toy Organizers",
                "category_parent_name": "Baby And Kids",
            },
            {"category_name": "Baby And Kids", "category_parent_name": None},
        ]
