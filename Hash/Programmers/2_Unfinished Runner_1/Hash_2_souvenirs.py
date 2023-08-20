def solution(participant, completion):
    participant.sort()
    completion.sort()
    '''
    for p, c in zip(participant, completion):
    # zip 함수 : 두 리스트의 같은 인덱스 값 -> 튜플화
        if p != c:
            return p
        
    return participant[-1]
    '''
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]

"""
만약 완주 못한 선수가 여러명이면...?
이 코드는 성립할까?
"""
