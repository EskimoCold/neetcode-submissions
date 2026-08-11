class Solution:
    def encode(self, strs: List[str]) -> str:
        replaced_strs = []
        
        for s in strs:
            if s == "":
                replaced_strs.append("<empty>")
            else:
                replaced_strs.append(s)
        
        return "<split>".join(replaced_strs)

    def decode(self, s: str) -> List[str]:
        res = []
        
        for el in s.split("<split>"):
            while "<empty>" in el:
                splitted = el.split("<empty>", maxsplit=1)
                print("splitted", splitted)
                
                if len(splitted[0]) > 0:
                    res.append(splitted[0])
                    
                res.append("")
                
                el = splitted[1]
                
            if len(el) > 0:
                res.append(el)
                
        return res
            