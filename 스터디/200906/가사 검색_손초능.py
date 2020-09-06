def add_word(_dict, w):
    if w not in _dict:
        _dict[w] = [0, {}]
    _dict[w][0] += 1
    return _dict[w][1]

def solution(words, queries):
    dict_front = {}
    dict_end = {}
    result = []

    for word in words:
        front = add_word(dict_front, len(word))
        end = add_word(dict_end, len(word))
        for i in range(len(word)):
            front = add_word(front, word[i])
            end = add_word(end, word[len(word)-i-1])

    for query in queries:
        _dict = dict_front
        if query[0] == '?':
            query = query[::-1]
            _dict = dict_end
        _dict = _dict.get(len(query), False)
        if _dict:
            for i in range(len(query)):
                if query[i] == '?' or i == len(query)-1:
                    result.append(_dict[0])
                    break
                else:
                    _dict = _dict[1].get(query[i], False)
                    if not _dict:
                        result.append(0)
                        break
        else: result.append(0)
    
    return result

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))  