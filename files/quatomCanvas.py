class test:
    z = [15, 75, 25, 45, 90, 5, 1, 4354, 2]
    newList = []

    def quatoum(self, ):
        print("hi")
        favorite_candy = ["chocolate", "peanut butter cups", "M&Ms"]
        favorite_candy.insert(2, "hello")
        print(favorite_candy)

    def find(self):
        z = [15, 75, 25, 45, 90, 5, 3]
        newList = []
        for x in z:
            if x < z[0] - 5:
                newList.append(x)
        print(newList)

    def block28(self):
        z = [15, 75, 25, 45, 90, 5, 1, 4354, 2]
        newList = []
        x = 0
        while x < len(z):
            try:
                if z[x] < z[x + 1]:
                    newList.append(z[x])
                x += 1
            except IndexError:
                print(newList)
                return 0

    def block30(self):
        z = [10, 2, 16, 827, 45,16,452,16, 34,35,23,45,62345345,432,524,35,234,5,234,5,123,41,2354,34,65,2456,435,6,234,5,2345,62,4562,43,52,345,234,6,456,2453,62,34,543,16,1,61,6,547,3,673,657,2356,45,646,57,3,73,546]
        newList = []
        x = 0
        while x < len(z):
            if z[x] == 16:
                newList.append(x)
                print("yes")
            else:
                print("nope")
            x += 1
        print(newList)
        return newList
    def test(self):
        print("worked")

class cool:
    def yes(self):
        print("yes")
