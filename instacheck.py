from instapy import InstaPy
from instapy.relationship_tools import (
    get_fans,
    get_followers,
    get_following,
    get_mutual_following,
    get_nonfollowers,
    get_unfollowers,
)

un = "thesqueakz"
pw = "Me147852"

session = InstaPy(username=un, password=pw, headless_browser=False, want_check_browser=False)
#session.login()

no_of_following = 772
no_of_followers = 817

followings = session.get_following('moustafaeledwy', no_of_following)
followers = session.grab_followers('moustafaeledwy', no_of_followers)

not_following = set(followings) - set(followers)

textfile = open("not_following.txt", "W")

for ff in not_following:
    print(ff)
    textfile.write(ff + "\n")
textfile.close()