# list_field_update_field()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 212–214 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L212-L214)
- **Module/theme:** list
- **Implements:** [hook_field_update_field()](../../../field.api.php/hook_field_update_field.md)

## Signature

```php
function list_field_update_field($field, $prior_field, $has_data)
```

## Documentation

```text
Implements hook_field_update_field().
```

## Code

```php
function list_field_update_field($field, $prior_field, $has_data) {
  drupal_static_reset('list_allowed_values');
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
