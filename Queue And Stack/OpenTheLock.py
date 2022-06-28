class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        
        def combinations(lock):                             # Helper funciton to create 8 possible combinations of each lock (+1 & -1 of each digit)
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)        # Add 1 to current index
                res.append(lock[:i] + digit + lock[i+1:])   # Create new combination replacing digit with previous value of index i
                digit = str((int(lock[i]) - 1 + 10) % 10)   # Subtract 1 from current index
                res.append(lock[:i] + digit + lock[i+1:])   # Create new combination replacing digit with previous value of index 
            return res                                      # Return list of combinations
        
        queue = deque()
        queue.append(["0000",0])                            # Keep track of turns with each Lock
        visited = set(deadends)                             # Track visited combinations and add deadends in it initially
        
        while queue:                                        
            lock, turns = queue.popleft()                   
            if lock == target: return turns                 # If current lock matches target, return turns it took to reach here
            for comb in combinations(lock):                 # Generate combinations of lock and traverse through them
                if comb not in visited:                     # If new combination is not visited before, add it to visited and queue
                    visited.add(comb)
                    queue.append([comb, turns +1])          # Add 1 to turns as it wil take one turn to move to either of these combinations
        return -1