def find_substring(str,substring):
    for word in str.split():
        if word == substring:
            return True
        
    else : 
        return False

str ="hello world pak"
#substring = "world"
split_str = str.split()
ans = find_substring(str,split_str[-1])

print(ans)
