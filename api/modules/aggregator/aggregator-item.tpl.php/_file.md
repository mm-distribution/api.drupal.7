# modules/aggregator/aggregator-item.tpl.php

- **Source:** [local](../../../../source/modules/aggregator/aggregator-item.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator-item.tpl.php) · 48 lines
- **Module/theme:** aggregator

## File documentation

```text
@file
Default theme implementation to format an individual feed item for display
on the aggregator page.

Available variables:
- $feed_url: URL to the originating feed item.
- $feed_title: Title of the feed item.
- $source_url: Link to the local source section.
- $source_title: Title of the remote source.
- $source_date: Date the feed was posted on the remote source.
- $content: Feed item content.
- $categories: Linked categories assigned to the feed.

@see template_preprocess()
@see template_preprocess_aggregator_item()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
