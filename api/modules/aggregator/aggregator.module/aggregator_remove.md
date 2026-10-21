# aggregator_remove()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 575–589 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L575-L589)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_remove($feed)
```

## Documentation

```text
Removes all items from a feed.

@param $feed
  An object describing the feed to be cleared.
```

## Code

```php
function aggregator_remove($feed) {
  _aggregator_get_variables();
  // Call hook_aggregator_remove() on all modules.
  module_invoke_all('aggregator_remove', $feed);
  // Reset feed.
  db_update('aggregator_feed')
    ->condition('fid', $feed->fid)
    ->fields(array(
      'checked' => 0,
      'hash' => '',
      'etag' => '',
      'modified' => 0,
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
