def pascals_traingle(no_of_rows):
    final_result=[]
    for i in range(no_of_rows):
        row=[1]
        for j in range(1,i):
            value=final_result[i-1][j-1]+final_result[i-1][j]
            row.append(value)
        if i>0:
            row.append(1)
        final_result.append(row)
    
    return final_result

if __name__=="__main__":
    print(pascals_traingle(4))
