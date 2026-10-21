# aggregator_aggregator_remove()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 53–65 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L53-L65)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_remove()](../aggregator.api.php/hook_aggregator_remove.md)

## Signature

```php
function aggregator_aggregator_remove($feed)
```

## Documentation

```text
Implements hook_aggregator_remove().
```

## Code

```php
function aggregator_aggregator_remove($feed) {
  $iids = db_query('SELECT iid FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchCol();
  if ($iids) {
    db_delete('aggregator_category_item')
      ->condition('iid', $iids, 'IN')
      ->execute();
  }
  db_delete('aggregator_item')
    ->condition('fid', $feed->fid)
    ->execute();

  drupal_set_message(t('The news items from %site have been removed.', array('%site' => $feed->title)));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
