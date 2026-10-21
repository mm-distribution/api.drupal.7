# modules/aggregator/aggregator-summary-items.tpl.php

- **Source:** [local](../../../../source/modules/aggregator/aggregator-summary-items.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator-summary-items.tpl.php) · 26 lines
- **Module/theme:** aggregator

## File documentation

```text
@file
Default theme implementation to present feeds as list items.

Each iteration generates a single feed source or category.

Available variables:
- $title: Title of the feed or category.
- $summary_list: Unordered list of linked feed items generated through
  theme_item_list().
- $source_url: URL to the local source or category.

@see template_preprocess()
@see template_preprocess_aggregator_summary_items()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
