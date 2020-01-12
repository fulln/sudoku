# -*- coding:utf-8 -*-


def remove_out(arrays,x,y,list=[]):
    '''
        删除数字，单个删除
    '''
    single_arr =  arrays[x][y]
    arrays[x][y] = set(single_arr) - set(list)
    if len(arrays[x][y]) == 1:
        return True
    return False    

def column_line_check(arrays,x,y,val):
    '''
        行或者列进行判断是否需要删除
    '''
    for i in range(9):
        check_single(arrays,x,i,val)
        check_single(arrays,i,y,val)

def check_single(arrays,x,y,val):
    '''
        单个位置的判断
    '''
    if not isinstance(arrays[x][y],int):
            if remove_out(arrays,x,y,[val]):
                list_val = arrays[x][y]
                range_check(arrays,x,y,list(list_val)[0])
                

def range_check(arrays,x,y,val):
    '''
        给2维数组中固定位置赋值成int 
     '''
    arrays[x][y] = val
    column_line_check(arrays,x,y,val)
    sudoku_check(arrays,x,y,val)
    # double_line_check(arrays,x,y,val)

def double_column_check(arrays,x,y,val):
    '''
    通过2个位置确定(判断规则)
    '''
    # for i in range(9):
    #     if len(arrays[x][y]) == 2:
    pass



def sudoku_check(arrays,x,y,val):
    '''
    九宫格判断是否需要删除
    '''
    for i in range(int(x/3)*3,(int(x/3)+1)*3):
        for j in range(int(y/3)*3,(int(y/3)+1)*3):
            check_single(arrays,i,j,val)

if __name__ == "__main__":    
    def_index = []
    for i in range(1,10):
        def_index.append(i)
    arr = []
    arr = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            arr[i][j] = def_index
            
    range_check(arr,1,1,3)
    range_check(arr,1,3,5)
    range_check(arr,1,7,6)
    range_check(arr,2,2,2)
    range_check(arr,2,4,8)
    range_check(arr,2,7,4)
    range_check(arr,3,1,5)
    range_check(arr,3,4,6)
    range_check(arr,3,7,8)
    range_check(arr,4,1,1)
    range_check(arr,4,4,7)
    range_check(arr,5,0,3)
    range_check(arr,5,4,2)
    range_check(arr,5,6,6)
    range_check(arr,5,7,7)
    range_check(arr,6,6,1)
    range_check(arr,6,8,7)
    range_check(arr,7,0,1)
    range_check(arr,7,3,8)
    range_check(arr,7,8,4)
    range_check(arr,8,1,4)
    range_check(arr,8,3,9)
    range_check(arr,8,7,3)

print(arr)

