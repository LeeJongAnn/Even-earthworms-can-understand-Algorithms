def solution(participant,completion):
    hashdict = {}
    sumHash = 0

    for part in participant:
        hashdict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)
    return hashdict[sumHash]
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"]
, ["josipa", "filipa", "marina", "nikola"]))