# modules/forum/forum-list.tpl.php

- **Source:** [local](../../../../source/modules/forum/forum-list.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum-list.tpl.php) · 78 lines
- **Module/theme:** forum

## File documentation

```text
@file
Displays a list of forums and containers.

Available variables:
- $forums: An array of forums and containers to display. It is keyed to the
  numeric IDs of all child forums and containers. Each $forum in $forums
  contains:
  - $forum->is_container: TRUE if the forum can contain other forums. FALSE
    if the forum can contain only topics.
  - $forum->depth: How deep the forum is in the current hierarchy.
  - $forum->zebra: 'even' or 'odd' string used for row class.
  - $forum->icon_class: 'default' or 'new' string used for forum icon class.
  - $forum->icon_title: Text alternative for the forum icon.
  - $forum->name: The name of the forum.
  - $forum->link: The URL to link to this forum.
  - $forum->description: The description of this forum.
  - $forum->new_topics: TRUE if the forum contains unread posts.
  - $forum->new_url: A URL to the forum's unread posts.
  - $forum->new_text: Text for the above URL, which tells how many new posts.
  - $forum->old_topics: A count of posts that have already been read.
  - $forum->num_posts: The total number of posts in the forum.
  - $forum->last_reply: Text representing the last time a forum was posted or
    commented in.
- $forum_id: Forum ID for the current forum. Parent to all items within the
  $forums array.

@see template_preprocess_forum_list()
@see theme_forum_list()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
