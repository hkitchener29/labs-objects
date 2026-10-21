"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    alice = User('alice')
    bob = User('bob')
    users = [alice, bob]

    posts = [
        Tweet('alice', 'Game night at my place Friday #Games #BringSnacks'),
        Tweet('bob', 'I will bring the chips and salsa'),
        Tweet('alice', 'Anyone have a copy of Catan? #Games'),
    ]

    # A small story: bob follows alice, changes his mind, then follows again.
    alice.follow()
    bob.follow()
    bob.unfollow()
    alice.follow()

    # The invitation gets two likes and one is taken back.
    posts[0].like()
    posts[0].like()
    posts[0].unlike()
    posts[2].like()

    return users, posts


def main():
    users, posts = build_feed()
    for user in users:
        print(user, '-', user.followers, 'followers')
    for post in posts:
        print(post)
        print('  likes:', post.likes)
        print('  hashtags:', post.hashtags())


if __name__ == '__main__':
    main()