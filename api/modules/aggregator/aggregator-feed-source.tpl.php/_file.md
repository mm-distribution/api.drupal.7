# modules/aggregator/aggregator-feed-source.tpl.php

- **Source:** [local](../../../../source/modules/aggregator/aggregator-feed-source.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator-feed-source.tpl.php) · 37 lines
- **Module/theme:** aggregator

## File documentation

```text
@file
Default theme implementation to present the source of the feed.

The contents are rendered above feed listings when browsing source feeds.
For example, "example.com/aggregator/sources/1".

Available variables:
- $source_icon: Feed icon linked to the source. Rendered through
  theme_feed_icon().
- $source_image: Image set by the feed source.
- $source_description: Description set by the feed source.
- $source_url: URL to the feed source.
- $last_checked: How long ago the feed was checked locally.

@see template_preprocess()
@see template_preprocess_aggregator_feed_source()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
