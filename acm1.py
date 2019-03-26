def is_junior(team):
    if (int(team.split(" ")[3]) == 1393 or int(team.split(" ")[3]) == 1394) and (
            int(team.split(" ")[4]) == 1393 or int(team.split(" ")[4]) == 1394) \
            and (int(team.split(" ")[5]) == 1393 or int(team.split(" ")[5]) == 1394):
        return True
    return False

n, q = input().split(" ")
n = int(n)
q = int(q)

team_list = list()
qualified_list = list()
for i in range(1, n + 1):
    team_list.append(input())

for s in team_list:
    if s.split(" ")[2] != "AUT":
        team_list.remove(s)

qualified_list = team_list[0:4]

flag = False
for team in qualified_list:
    if is_junior(team):
        qualified_list.append(team_list[4])
        break
    else:
        for junior in team_list[4:]:
            # print(junior)
            if is_junior(junior):
                qualified_list.append(junior)
                flag = True
                break
    if flag:
        break

if len(qualified_list) == 4:
    qualified_list.append(team_list[4])

for team in qualified_list:
    print(team.split(" ")[1])
