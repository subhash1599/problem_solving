def can_place_flowers(flower_bed,new_flowers):
    count=0
    flower_bed=[0]+flower_bed+[0]
    for i in range(len(flower_bed)):
        if i<=len(flower_bed):
            if flower_bed[i]==0 and flower_bed[i-1]!=1 and flower_bed[i+1]!=1:
                flower_bed[i]=1
                count+=1
    return count>=new_flowers

if __name__=="__main__":
    print(can_place_flowers([1,0,0,0,1],1))
        