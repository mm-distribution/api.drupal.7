# block_add_block_form_validate()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 537–543 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L537-L543)
- **Module/theme:** block

## Signature

```php
function block_add_block_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for block_add_block_form().

@see block_add_block_form()
@see block_add_block_form_submit()
```

## Code

```php
function block_add_block_form_validate($form, &$form_state) {
  $custom_block_exists = (bool) db_query_range('SELECT 1 FROM {block_custom} WHERE info = :info', 0, 1, array(':info' => $form_state['values']['info']))->fetchField();

  if (empty($form_state['values']['info']) || $custom_block_exists) {
    form_set_error('info', t('Ensure that each block description is unique.'));
  }
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
