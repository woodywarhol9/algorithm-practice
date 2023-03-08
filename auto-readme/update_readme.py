from git import Repo

repo = Repo.init("../")
branch_now = repo.active_branch# 현재 Branch 이름
files = repo.git.diff([f"{branch_now}..origin/{branch_now}"], name_only = True)
print(branch_now)
print(branch_now.commit)
#for commit in list(repo.iter_commits()):
#    print(commit.stats.files(name_only = True))
#branch_now = repo.active_branch# 현재 Branch 이름
#print(branch_now.commit)
#files = repo.git.diff([f"{branch_now}..origin/main"], name_only = True)
#print(files)