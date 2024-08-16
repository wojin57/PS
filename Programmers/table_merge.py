# https://school.programmers.co.kr/learn/courses/30/lessons/150366
# helper function for searching indexes of the vertices in the merge table
def Indexing(table, value):
    for i in range(len(table)):
        if value in table[i]:
            return i
    return -1


def Update(cells, merge_table, args):
    # UPDATE r c value
    if len(args) == 3:
        r, c, value = int(args[0]), int(args[1]), args[2]
        cells[r][c] = value
        
        # if the cell is merged, manage them altogether
        if (i := Indexing(merge_table, (r, c))) != -1:
            for i, j in merge_table[i]:
                cells[i][j] = value
            
    
    # UPDATE value1 value2
    elif len(args) == 2:
        value1, value2 = args
        for i in range(51):
            for j in range(51):
                if cells[i][j] == value1:
                    cells[i][j] = value2
    
    
def Merge(cells, merge_table, args):
    r1, c1, r2, c2 = [int(i) for i in args]
    # ignore if two cells are same
    if (r1, c1) == (r2, c2):
        return
    
    # update the merge table
    if (i1 := Indexing(merge_table, (r1, c1))) != -1:
        if (i2 := Indexing(merge_table, (r2, c2))) != -1:
            if i1 == i2: # exit if already merged
                return
            merge_table[i1] = merge_table[i1] + merge_table[i2]
            merge_table.remove(merge_table[i2])
        else:
            merge_table[i1].append((r2, c2))
    else:
        if (i2 := Indexing(merge_table, (r2, c2))) != -1:
            merge_table[i2].append((r1, c1))
        else:
            merge_table.append([(r1, c1), (r2, c2)])
        
    # update the value of cells
    for r, c in merge_table[Indexing(merge_table, (r1, c1))]:
        if cells[r1][c1] == "EMPTY":
            cells[r][c] = cells[r2][c2]
        else:
            cells[r][c] = cells[r1][c1]

    
def Unmerge(cells, merge_table, args):
    r, c = [int(i) for i in args]
    for merged_cells in merge_table:
        if (r, c) in merged_cells:
            for i, j in merged_cells:
                if (r, c) != (i, j):
                    cells[i][j] = "EMPTY"
            merge_table.remove(merged_cells)
            
    
def Print(answer, cells, args):
    r, c = [int(i) for i in args]
    answer.append(cells[r][c])


def solution(commands):
    answer = []
    cells = [["EMPTY" for _ in range(51)] for _ in range(51)]
    merge_table = []
    for command in commands:
        com, *args = command.split(" ")
        if com == "UPDATE":
            Update(cells, merge_table, args)
        elif com == "MERGE":
            Merge(cells, merge_table, args)
        elif com == "UNMERGE":
            Unmerge(cells, merge_table, args)
        elif com == "PRINT":
            Print(answer, cells, args)
    return answer


if __name__ == '__main__':
    print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))