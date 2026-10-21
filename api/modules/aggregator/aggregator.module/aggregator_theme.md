# aggregator_theme()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 50–93 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L50-L93)
- **Module/theme:** aggregator
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function aggregator_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function aggregator_theme() {
  return array(
    'aggregator_wrapper' => array(
      'variables' => array('content' => NULL),
      'file' => 'aggregator.pages.inc',
      'template' => 'aggregator-wrapper',
    ),
    'aggregator_categorize_items' => array(
      'render element' => 'form',
      'file' => 'aggregator.pages.inc',
    ),
    'aggregator_feed_source' => array(
      'variables' => array('feed' => NULL),
      'file' => 'aggregator.pages.inc',
      'template' => 'aggregator-feed-source',
    ),
    'aggregator_block_item' => array(
      'variables' => array('item' => NULL, 'feed' => 0),
    ),
    'aggregator_summary_items' => array(
      'variables' => array('summary_items' => NULL, 'source' => NULL),
      'file' => 'aggregator.pages.inc',
      'template' => 'aggregator-summary-items',
    ),
    'aggregator_summary_item' => array(
      'variables' => array('item' => NULL),
      'file' => 'aggregator.pages.inc',
      'template' => 'aggregator-summary-item',
    ),
    'aggregator_item' => array(
      'variables' => array('item' => NULL),
      'file' => 'aggregator.pages.inc',
      'template' => 'aggregator-item',
    ),
    'aggregator_page_opml' => array(
      'variables' => array('feeds' => NULL),
      'file' => 'aggregator.pages.inc',
    ),
    'aggregator_page_rss' => array(
      'variables' => array('feeds' => NULL, 'category' => NULL),
      'file' => 'aggregator.pages.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
