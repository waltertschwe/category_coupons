from datetime import datetime
from typing import List

from model import CategoryModel, CouponModel


class Coupon:
    """
    Coupon generic class.
    """

    def __init__(self):
        self.coupon_data = CouponModel().get_coupon_data()

    def get_coupon_data(self):
        """
        Get coupon data from Coupon Model
        """
        return self.coupon_data

    def get_coupons_for_category(self, category_name: str) -> List[dict]:
        """
        Get coupons for a given category.
        """
        return [
            coupon
            for coupon in self.get_coupon_data()
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


class App:
    """
    Category to Coupon App
    """

    def __init__(self):
        self.coupon = Coupon()
        self.category = Category()

    def get_coupons_for_all_categories(self):
        """
        For all categories attempt to find coupon(s).
        """
        for category in self.category.get_category_data():
            coupon_result = self.coupon.get_coupons_for_category(
                category["category_name"]
            )

            # no result so let's search the parent category for results
            if not coupon_result:
                coupon_result = self.coupon.get_coupons_for_category(
                    category["category_parent_name"]
                )

            # more than one result let's sort the coupons.
            if len(coupon_result) > 1:
                coupon_result = self.coupon.sort_coupons_by_date_field(
                    coupon_result, "date_modified", True
                )
            else:
                # we only found one coupon or none. let's show that coupon no reason to sort on one or zero results.
                coupon_result = (
                    coupon_result["coupon_name"]
                    if "coupon_name" in coupon_result
                    else []
                )
            print(f'Category Name = {category["category_name"]} => {coupon_result}')


if __name__ == "__main__":  # pragma: no cover
    app = App()
    app.get_coupons_for_all_categories()
