find_dup=lambda arr:{v:k for k,v in dict(__import__("collections").Counter(arr)).items() if v % 2 == 0}.get(2)
