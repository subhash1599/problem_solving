def kids_with_candies(candies,extra_candies):
    result=[False]*len(candies)
    total_candies=0
    max_candy=max(candies)
    for i in range(len(candies)):
        total_candies=extra_candies+candies[i]
        if total_candies>=max_candy:
            result[i]=True 
    return result

if __name__=="__main__":
    print(kids_with_candies([2,3,5,1,3],3))
    