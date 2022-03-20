'''

TC: O(k ^ (n - k)) - k average length of braces
SC: O(n - k)

'''
class Solution:
    def expand(self, s: str) -> List[str]:
        slen = len(s)
        res = list()
        
        def rec(arr, res, i, curr):
            if i >= slen:
                res.append(curr)
                return
            options = list()
            
            if arr[i] == "{":
                i += 1
                
                while i < slen and arr[i] != "}":
                    if arr[i] != ",":
                        options.append(arr[i])
                    i += 1
                    
            if not options:
                rec(arr, res, i + 1, curr + (arr[i] if arr[i] != "," else ""))
            else:
                for op in options:
                    rec(arr, res, i + 1, curr + op)
        
        rec(s, res, 0, "")
        
        return sorted(res)