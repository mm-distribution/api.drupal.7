# list_field_is_empty()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 408–413 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L408-L413)
- **Module/theme:** list
- **Implements:** [hook_field_is_empty()](../../../field.api.php/hook_field_is_empty.md)

## Signature

```php
function list_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function list_field_is_empty($item, $field) {
  if (empty($item['value']) && (string) $item['value'] !== '0') {
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
