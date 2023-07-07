import copy
file=[[1, 0 ,0 ,2 ,4],
      [2, 0 ,1 ,3 ],
      [3, 0 ,2 ],
      [4, -0.5 ,0 ,6],
      [5, -0.1 ,0.1 ,6],
      [6, -0.5,-0.5,1]]
# file=[[1, 0 ,0 ,2 ,3],
#       [2, 0 ,1 ],
#       [3, 0 ,2,1 ]]

def SmurfTown(file):
    path=[]
    for i in range(len(file)):
        a = []
        seen = []
        Q=0
        name_ = copy.deepcopy(file[i][0])
        W=1
        seen.append(name_)
        a.append(name_)
        while W==1:
            name_len=len(file[name_-1])
            if name_len==5:
                first=file[name_-1][3]
                second=file[name_-1][4]
                Q=1

                if a[0]==first:
                    a.append(first)
                    path.append(a)
                    break
                if (first in seen) == 0:
                    seen_ = copy.deepcopy(seen)
                    a_ = copy.deepcopy(a)
                    seen.append(first)
                    a.append(first)
                    name_=first
                elif (first in seen)==1:
                    break

            if name_len==4:
                first=file[name_-1][3]
                if a[0]==first:
                    a.append(first)
                    path.append(a)
                    break
                if (first in seen)==0:
                    a.append(first)
                    seen.append(first)
                    name_=first
                elif (first in seen)==1:
                    break
            if name_len <4 and Q==1:
                seen=copy.deepcopy(seen_)
                a=copy.deepcopy(a_)
                if a[0] == second:
                    a.append(second)
                    path.append(a)
                    break
                if (second in seen)==0:
                    seen.append(second)
                    a.append(second)
                    name_ = second
                elif (second in seen)==1:
                    break
            elif name_len<4:
                W=0

    return path



if __name__ == '__main__':
    print(SmurfTown(file))

