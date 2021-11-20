#!/usr/bin/env python3

from datetime import datetime, timedelta
import random
from faker import Faker
from app import wep_create_app
from app.models import db
from app.models.WEPUser import WEPUser
from app.models.WEPPost import WEPPost
from app.models.WEPCategory import WEPCategory, post_categories
from app.models.WEPTag import WEPTag, post_tags


POST_COUNT = 50
CATEGORY_COUNT = 25
TAG_COUNT = 100

# Time began on January 1, 1970, at 0:00 UTC
TIME_START = datetime(1970, 1, 1, 0, 0, 0, 0)
TIME_END = datetime.now()


def random_date():
    return TIME_START + timedelta(days=random.randrange((TIME_END - TIME_START).days))


def truncate_tables():
    db.session.execute(post_categories.delete())
    WEPPost.query.delete()
    WEPCategory.query.delete()
    db.session.commit()


def main():
    app = wep_create_app(True)
    app.app_context().push()
    truncate_tables()
    fake = Faker()
    author = WEPUser("wae", "hunter2", "itdoesnthavetomakesense",
                   "nobody@example.com", "/images/nobodyman.jpg")

    db.session.add(author)
    db.session.commit()


    with open('./tools/wordlist.10000', 'r') as fh:
        words = fh.readlines()
        wordlist = [w.rstrip() for w in words if len(w) >= 5]

    for _ in range(POST_COUNT):
        create_date = random_date()
        publish_date = random_date()
        modify_date = random_date()
        title_str = " ".join(random.sample(wordlist, random.randint(3, 7))).title()
        content = "\n\n".join(fake.paragraphs(10))
        summary = fake.paragraph()

        post = WEPPost(is_published=True,
                       publish_date=publish_date,
                       create_date=create_date,
                       modify_date=modify_date,
                       name=title_str,
                       content=content,
                       summary=summary,
                       author=author.user_id)
        db.session.add(post)

    db.session.commit()

    for _ in range(CATEGORY_COUNT):
        create_date = random_date()
        publish_date = random_date()
        modify_date = random_date()
        title_str = " ".join(random.sample(wordlist, random.randint(1, 2))).title()
        summary = fake.paragraph()

        category = WEPCategory(is_published=True,
                               publish_date=publish_date,
                               create_date=create_date,
                               modify_date=modify_date,
                               name=title_str,
                               summary=summary,
                               parent=None)
        db.session.add(category)

    for _ in range(TAG_COUNT):
        create_date = random_date()
        publish_date = random_date()
        modify_date = random_date()
        title_str = " ".join(random.sample(wordlist, random.randint(1, 2))).title()
        summary = fake.paragraph()

        tag = WEPTag(is_published=True,
                     publish_date=publish_date,
                     create_date=create_date,
                     modify_date=modify_date,
                     name=title_str,
                     summary=summary)
        db.session.add(tag)

    db.session.commit()

    post_category_pairs = set()
    while len(post_category_pairs) < POST_COUNT * 2:
        candidate = (
            random.randint(1, POST_COUNT),
            random.randint(1, CATEGORY_COUNT)
        )

        if candidate in post_category_pairs:
            continue

        post_category_pairs.add(candidate)

    new_categories = [
        {"post_id": pair[0], "category_id": pair[1]}
        for pair in list(post_category_pairs)
    ]
    insert_postcats_query = post_categories.insert().values(new_categories)

    post_tag_pairs = set()
    while len(post_tag_pairs) <= POST_COUNT * 4:
        candidate = (
            random.randint(1, POST_COUNT),
            random.randint(1, TAG_COUNT)
        )

        if candidate in post_tag_pairs:
            continue

        post_tag_pairs.add(candidate)

    new_tags = [
        {"post_id": pair[0], "tag_id": pair[1]}
        for pair in list(post_category_pairs)
    ]
    insert_posttags_query = post_tags.insert().values(new_tags)

    db.session.execute(insert_postcats_query)
    db.session.execute(insert_posttags_query)
    db.session.commit()


if __name__ == '__main__':
    main()
