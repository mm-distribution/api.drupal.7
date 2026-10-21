# aggregator_block_configure()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 364–376 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L364-L376)
- **Module/theme:** aggregator
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function aggregator_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function aggregator_block_configure($delta = '') {
  list($type, $id) = explode('-', $delta);
  if ($type == 'category') {
    $value = db_query('SELECT block FROM {aggregator_category} WHERE cid = :cid', array(':cid' => $id))->fetchField();
    $form['block'] = array(
      '#type' => 'select',
      '#title' => t('Number of news items in block'),
      '#default_value' => $value,
      '#options' => drupal_map_assoc(range(2, 20)),
    );
    return $form;
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
