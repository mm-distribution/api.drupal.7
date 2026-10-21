# block_admin_configure_validate()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 448–458 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L448-L458)
- **Module/theme:** block

## Signature

```php
function block_admin_configure_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for block_admin_configure().

@see block_admin_configure()
@see block_admin_configure_submit()
```

## Code

```php
function block_admin_configure_validate($form, &$form_state) {
  if ($form_state['values']['module'] == 'block') {
    $custom_block_exists = (bool) db_query_range('SELECT 1 FROM {block_custom} WHERE bid <> :bid AND info = :info', 0, 1, array(
      ':bid' => $form_state['values']['delta'],
      ':info' => $form_state['values']['info'],
    ))->fetchField();
    if (empty($form_state['values']['info']) || $custom_block_exists) {
      form_set_error('info', t('Ensure that each block description is unique.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
