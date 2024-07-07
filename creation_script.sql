BEGIN;
--
-- Create model Topic
--
CREATE TABLE "forum_topic" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(100) NOT NULL,
    "content" text NOT NULL,
    "date_posted" datetime NOT NULL,
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
)
CREATE INDEX "forum_topic_author_id_69c0a4d8" ON "forum_topic" ("author_id");
COMMIT;