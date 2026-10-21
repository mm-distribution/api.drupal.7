# number_field_is_empty()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 181–186 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L181-L186)
- **Module/theme:** number
- **Implements:** [hook_field_is_empty()](../../../field.api.php/hook_field_is_empty.md)

## Signature

```php
function number_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function number_field_is_empty($item, $field) {
  if (empty($item['value']) && (string) $item['value'] !== '0') {
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
