# aggregator_block_save()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 381–389 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L381-L389)
- **Module/theme:** aggregator
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function aggregator_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function aggregator_block_save($delta = '', $edit = array()) {
  list($type, $id) = explode('-', $delta);
  if ($type == 'category') {
    db_update('aggregator_category')
      ->fields(array('block' => $edit['block']))
      ->condition('cid', $id)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
