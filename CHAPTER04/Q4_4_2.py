def vote(vote_n):
    print("投票します")
    vote_n += 1
    return vote_n


def reset_box(vote_n):
    print("箱を空にします")
    vote_n = 0
    return vote_n


def check_box(vote_n):
    print("表の数は{}です".format(vote_n))


vote_num = 0
vote_num = vote(vote_num)
print("箱を空にします")
vote_num = reset_box(vote_num)
check_box(vote_num)
