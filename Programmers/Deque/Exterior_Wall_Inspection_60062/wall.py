from itertools import combinations

def solution():

    n = 10
    weak = [2,5,7,10,18]
    dist = [9,10,14]
    distances = []
    Run = []
    # Calculate distances
    for a in range(1,len(weak)):
        distance = abs(weak[a] - weak[a-1])
        distances.append(distance)

    # 거리들을 콤비네이션으로 묶음
    for i in range(len(distances),0,-1):
        combi = list(combinations(distances,i))
        print("combinations are",combi)
        # 가능한 거리 조합을 더함
        for a in range(len(list(combi))):
            trav = sum((combi[a]))
            Run.append(trav)
        Run.sort()
        print("Run is", Run)
        Run=[]
        """
            for vel in range(0,len(dist),-1):
                if dist[vel] > trav:
                    dist.pop()
                else:
                    break
        """



    #return (list(combi))

if __name__  == "__main__" :
    print(solution())