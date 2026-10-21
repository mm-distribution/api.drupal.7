# modules/announcements_feed/announcements-feed.tpl.php

- **Source:** [local](../../../../source/modules/announcements_feed/announcements-feed.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements-feed.tpl.php) · 72 lines
- **Module/theme:** announcements_feed

## File documentation

```text
@file
Template file for the theming of announcements_feed admin page.

Available variables:
- $count: Contains the total number of announcements.
- $featured: An array of featured announcements.
- $standard: An array of non-featured announcements.

Each $announcement in $featured and $standard contain:
- $announcement['id']: Unique id of the announcement.
- $announcement['title']: Title of the announcement.
- $announcement['teaser']: Short description of the announcement.
- $announcement['link']: Learn more link of the announcement.
- $announcement['date_published']: Timestamp of the announcement.

@see announcements_feed_theme()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
