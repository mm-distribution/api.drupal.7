# modules/aggregator/aggregator.module

- **Source:** [local](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · 791 lines
- **Module/theme:** aggregator

## File documentation

```text
@file
Used to aggregate syndicated content (RSS, RDF, and Atom).
```

## Functions (derived index)

- [aggregator_help()](aggregator_help.md) — Implements hook_help().
- [aggregator_theme()](aggregator_theme.md) — Implements hook_theme().
- [aggregator_menu()](aggregator_menu.md) — Implements hook_menu().
- [_aggregator_category_title()](_aggregator_category_title.md) — Title callback: Returns a title for aggregator category pages.
- [_aggregator_has_categories()](_aggregator_has_categories.md) — Determines whether there are any aggregator categories.
- [aggregator_permission()](aggregator_permission.md) — Implements hook_permission().
- [aggregator_cron()](aggregator_cron.md) — Implements hook_cron().
- [aggregator_cron_queue_info()](aggregator_cron_queue_info.md) — Implements hook_cron_queue_info().
- [aggregator_block_info()](aggregator_block_info.md) — Implements hook_block_info().
- [aggregator_block_configure()](aggregator_block_configure.md) — Implements hook_block_configure().
- [aggregator_block_save()](aggregator_block_save.md) — Implements hook_block_save().
- [aggregator_block_view()](aggregator_block_view.md) — Implements hook_block_view().
- [aggregator_save_category()](aggregator_save_category.md) — Adds/edits/deletes aggregator categories.
- [aggregator_save_feed()](aggregator_save_feed.md) — Add/edit/delete an aggregator feed.
- [aggregator_remove()](aggregator_remove.md) — Removes all items from a feed.
- [_aggregator_get_variables()](_aggregator_get_variables.md) — Gets the fetcher, parser, and processors.
- [aggregator_refresh()](aggregator_refresh.md) — Checks a news feed for new items.
- [aggregator_feed_load()](aggregator_feed_load.md) — Loads an aggregator feed.
- [aggregator_category_load()](aggregator_category_load.md) — Loads an aggregator category.
- [theme_aggregator_block_item()](theme_aggregator_block_item.md) — Returns HTML for an individual feed item for display in the block.
- [aggregator_filter_xss()](aggregator_filter_xss.md) — Renders the HTML content safely, as allowed.
- [aggregator_sanitize_configuration()](aggregator_sanitize_configuration.md) — Checks and sanitizes the aggregator configuration.
- [_aggregator_items()](_aggregator_items.md) — Helper function for drupal_map_assoc.

## Constants

### AGGREGATOR_CLEAR_NEVER

- Line 11

```php
define('AGGREGATOR_CLEAR_NEVER', 0);
```

```text
Denotes that a feed's items should never expire.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
