class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {} # Positions of first & last occurrances of the unique letter
        '''
        pos = {
            "x": [0, 3],
            "y": [2, 4], -> [0, 4] {5}
            "z": [5, 7],
            ...
            }
        '''
        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = [i, i]
                continue
            pos[ch][1] = i
    
        pos_values = list(pos.values())
        first_idx = pos_values[0][0]
        last_idx = pos_values[0][1]
        res = []

        
        for x, y in pos_values[1:]:
            if x < last_idx:
                last_idx = y if y > last_idx else last_idx
                continue
            substr_len = last_idx - first_idx + 1
            res.append(substr_len)

            first_idx = x
            last_idx = y if y != -1 else x

        res.append(last_idx - first_idx + 1)
        return res           