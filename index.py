from datetime import datetime
from typing import List

from model import CategoryModel, CouponModel


class Coupon:
    """
    Coupon specific features.
    """

    def __init__(self):
        """
        Coupon Class initilization - get coupon data.
        """
        self.coupon_data = CouponModel().get_coupoun_data()

    def get_coupons_for_category(self, category_name: str) -> List[dict]:
        """
        Get coupons for a given category.
        """
        return [
            coupon
            for coupon in self.coupon_data
            if coupon["category_name"] == category_name
        ]

    def sort_coupons_by_date_field(
        self, coupons: List[dict], sort_field: str, most_recent: bool = True
    ) -> List[dict]:
        """
        Sort a List of coupons by a defined date_field
        """
        coupons.sort(
            key=lambda o: datetime.strptime(o[sort_field], "%Y-%m-%d"),
            reverse=most_recent,
        )
        return [coupon["coupon_name"] for coupon in coupons]


class Category:
    """
    Category specific features.
    """

    def __init__(self):
        self.category_data = CategoryModel().get_category_data()

    def get_category_data(self) -> List[dict]:
        """
        Get all category data
        """
        return self.category_data



if __name__ == "__main__":
    coupon = Coupon()
    category = Category()
    for category in category.category_data:
        coupon_result = coupon.get_coupons_for_category(category["category_name"])
        if not coupon_result:
            coupon_result = coupon.get_coupons_for_category(
                category["category_parent_name"]
            )

        if len(coupon_result) > 1:
            coupon_result = coupon.sort_coupons_by_date_field(
                coupon_result, "date_modified", True
            )
        else:
            coupon_result = (
                coupon_result["coupon_name"] if "coupon_name" in coupon_result else []
            )

        print(f'Category Name = {category["category_name"]} => {coupon_result}')
