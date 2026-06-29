class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #find distance from origin for each point
        #sort distances
        #return first k values

        list_of_distances = []

        for point in points:
            distance = math.sqrt(math.pow((point[0] - 0), 2) + math.pow(point[1] - 0, 2))
            list_of_distances.append([distance, point])

        sorted_distances = sorted(list_of_distances, key = lambda distances:distances[0])


        answer = []
        counter = 0
        while k != 0:
            answer.append(sorted_distances[counter][1])
            counter += 1
            k -= 1

        return answer
