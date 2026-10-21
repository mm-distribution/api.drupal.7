# block_admin_display_form_submit()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 172–197 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L172-L197)
- **Module/theme:** block

## Signature

```php
function block_admin_display_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for block_admin_display_form().

@see block_admin_display_form()
```

## Code

```php
function block_admin_display_form_submit($form, &$form_state) {
  $transaction = db_transaction();
  try {
    foreach ($form_state['values']['blocks'] as $block) {
      $block['status'] = (int) ($block['region'] != BLOCK_REGION_NONE);
      $block['region'] = $block['status'] ? $block['region'] : '';
      db_update('block')
        ->fields(array(
          'status' => $block['status'],
          'weight' => $block['weight'],
          'region' => $block['region'],
        ))
        ->condition('module', $block['module'])
        ->condition('delta', $block['delta'])
        ->condition('theme', $block['theme'])
        ->execute();
    }
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('block', $e);
    throw $e;
  }
  drupal_set_message(t('The block settings have been updated.'));
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
