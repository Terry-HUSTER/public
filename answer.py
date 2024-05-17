#question 1
def subsequence_counts(source, target):
    #判断是否有source中未出现字符
    st = set(source)
    for char in target:
        if char not in st:
            return -1
    
    count = 0
    i = 0

    while i < len(target):
        j = 0
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                i += 1
            j += 1
        count += 1

    return count



#question 2
def check_parentheses(input):
    results = []
    for line in input:
        left_count = 0
        stack = []
        markers = [' '] * len(line)
        
        #第一遍遍历，匹配左右括号，多余的左括号存储下标
        for i, char in enumerate(line):
            if char == '(':
                left_count += 1
                stack.append(i)
            elif char == ')':
                if left_count > 0:
                    left_count -= 1
                    stack.pop()
                else:
                    markers[i] = '?'
        
        #每行弹出剩余左括号
        while stack:
            markers[stack.pop()] = 'x'
        

        results.append(line)
        results.append(''.join(markers))#生成字符串
    
    return results