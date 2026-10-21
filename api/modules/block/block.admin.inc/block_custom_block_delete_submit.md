# block_custom_block_delete_submit()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 635–651 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L635-L651)
- **Module/theme:** block

## Signature

```php
function block_custom_block_delete_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for block_custom_block_delete().

@see block_custom_block_delete()
```

## Code

```php
function block_custom_block_delete_submit($form, &$form_state) {
  db_delete('block_custom')
    ->condition('bid', $form_state['values']['bid'])
    ->execute();
  db_delete('block')
    ->condition('module', 'block')
    ->condition('delta', $form_state['values']['bid'])
    ->execute();
  db_delete('block_role')
    ->condition('module', 'block')
    ->condition('delta', $form_state['values']['bid'])
    ->execute();
  drupal_set_message(t('The block %name has been removed.', array('%name' => $form_state['values']['info'])));
  cache_clear_all();
  $form_state['redirect'] = 'admin/structure/block';
  return;
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
