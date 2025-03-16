class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right =min(ranks)*cars*cars
        def repaired_cars(time):
            required_car = 0
            for rank in ranks:
                total_cars = int((time/rank)**0.5)
                required_car += total_cars
                if required_car >= cars:
                    return True
            return False

        while left < right:
            mid = (left+right)//2
            if repaired_cars(mid):
                right = mid
            else:
                left =mid+1
        return left                

        