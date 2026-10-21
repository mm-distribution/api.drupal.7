# list_field_update_forbid()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 358–366 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L358-L366)
- **Module/theme:** list
- **Implements:** [hook_field_update_forbid()](../../../field.api.php/hook_field_update_forbid.md)

## Signature

```php
function list_field_update_forbid($field, $prior_field, $has_data)
```

## Documentation

```text
Implements hook_field_update_forbid().
```

## Code

```php
function list_field_update_forbid($field, $prior_field, $has_data) {
  if ($field['module'] == 'list' && $has_data) {
    // Forbid any update that removes allowed values with actual data.
    $lost_keys = array_diff(array_keys($prior_field['settings']['allowed_values']), array_keys($field['settings']['allowed_values']));
    if (_list_values_in_use($field, $lost_keys)) {
      throw new FieldUpdateForbiddenException(t('A list field (@field_name) with existing data cannot have its keys changed.', array('@field_name' => $field['field_name'])));
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
