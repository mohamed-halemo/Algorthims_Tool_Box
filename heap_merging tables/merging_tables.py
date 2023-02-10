# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts#row counts
        self.max_row_count = max(row_counts)#max row  count
        n_tables = len(row_counts)#tables number
        self.ranks = [1] * n_tables #ranks 
        self.parents = list(range(n_tables)) #parents list

    def merge(self, src, dst):
        #get source parent and destination parent (link)
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        #if src and destination are same return false (as source is destination now)
        if src_parent == dst_parent:
            return False
        #now check rank which is higher and put it as parent and the other as destination
      
        else:# else
            self.parents[src_parent] = dst_parent #change parent of src to dst
            self.row_counts[dst_parent] += self.row_counts[src_parent]#increase row count of dst
            self.row_counts[src_parent] = 0 #set rows to zero as we added them up to dst
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])#update maximum
            # if both ranks are same
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1 #Increase Rank of dst
        
        return True

    def get_parent(self, table):
        #check if data exist in that table if not get it's parent
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        # find parent and compress path
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
