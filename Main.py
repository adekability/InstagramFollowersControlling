import instaloader

L = instaloader.Instaloader()
L.login("adekability", "password")
profile = instaloader.Profile.from_username(L.context, "adekability")
followees = []
followers = []

for followee in profile.get_followees():
    followees.append(followee.username)
for follower in profile.get_followers():
    followers.append(follower.username)
for i in followees:
    if followers.__contains__(i):
        followers.remove(i)

print(followers)