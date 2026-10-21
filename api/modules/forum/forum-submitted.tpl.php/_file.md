# modules/forum/forum-submitted.tpl.php

- **Source:** [local](../../../../source/modules/forum/forum-submitted.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum-submitted.tpl.php) · 31 lines
- **Module/theme:** forum

## File documentation

```text
@file
Formats a forum post submission string.

The submission string indicates when and by whom a topic was submitted.

Available variables:
- $author: The author of the post.
- $time: How long ago the post was created.
- $topic: An object with the raw data of the post. Potentially unsafe. Be
  sure to clean this data before printing.

@see template_preprocess_forum_submitted()
@see theme_forum_submitted()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
