# _aggregator_page_list()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 173–188 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L173-L188)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_page_list($items, $op, $feed_source = '')
```

## Documentation

```text
Prints an aggregator page listing a number of feed items.

Various menu callbacks use this function to print their feeds.

@param $items
  The items to be listed.
@param $op
  Which form should be added to the items. Only 'categorize' is now
  recognized.
@param $feed_source
  The feed source URL.

@return
  The rendered list of items for the feed.
```

## Code

```php
function _aggregator_page_list($items, $op, $feed_source = '') {
  if (user_access('administer news feeds') && ($op == 'categorize')) {
    // Get form data.
    $output = aggregator_categorize_items($items, $feed_source);
  }
  else {
    // Assemble themed output.
    $output = $feed_source;
    foreach ($items as $item) {
      $output .= theme('aggregator_item', array('item' => $item));
    }
    $output = theme('aggregator_wrapper', array('content' => $output));
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
