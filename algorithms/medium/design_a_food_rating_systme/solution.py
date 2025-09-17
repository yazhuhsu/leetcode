class FoodRatings:

    def __init__(self, foods: list, cuisines: list, ratings: list):
        self.cuisines = {}
        self.ratings = {}

        for _, cuisine in enumerate(set(cuisines)):
            self.cuisines[cuisine] = []
        
        for idx, food in enumerate(foods):
            self.cuisines[cuisines[idx]].append(food)

        for idx, rate in enumerate(ratings):
            self.ratings[foods[idx]] = rate
            
        self.ratings = dict(sorted(self.ratings.items(), key=lambda item: item[1], reverse=True))

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        highest_rate, highest_food = 0, ''

        for _, food in enumerate(sorted(self.cuisines[cuisine], reverse=True)):
            if self.ratings[food] >= highest_rate:
                highest_rate = self.ratings[food]
                highest_food = food

        return highest_food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
cuisines = ["korean","japanese","japanese","greek","japanese","korean"]
ratings = [9,12,8,15,14,7]

object = FoodRatings(foods, cuisines, ratings)
print(object.highestRated("korean") == "kimchi")
print(object.highestRated("japanese") == "ramen")
object.changeRating("sushi", 16)
print(object.highestRated("japanese") == "sushi")
object.changeRating("ramen", 16)
print(object.highestRated("japanese") == "ramen")