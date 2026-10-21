# block_add_block_form()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 527–529 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L527-L529)
- **Module/theme:** block
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function block_add_block_form($form, &$form_state)
```

## Documentation

```text
Form constructor for the add block form.

@see block_add_block_form_validate()
@see block_add_block_form_submit()
@ingroup forms
```

## Code

```php
function block_add_block_form($form, &$form_state) {
  return block_admin_configure($form, $form_state, 'block', NULL);
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
