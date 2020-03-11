n = int(input())
s = set(map(int, input().split()))

############################# my code ###########################
number_of_commits = int(input())

for i in range(number_of_commits):
    commit = input().split()

    try:
        if commit[0] == "remove":
            s.remove(int(commit[1]))
        elif commit[0] == "discard":
            s.remove(int(commit[1]))
        else:
            s.pop()
    except KeyError:
        pass

print(sum(s))
##########################  end of my code ########################