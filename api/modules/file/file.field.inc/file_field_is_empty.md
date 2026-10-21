# file_field_is_empty()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 376–378 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L376-L378)
- **Module/theme:** file
- **Implements:** [hook_field_is_empty()](../../field/field.api.php/hook_field_is_empty.md)

## Signature

```php
function file_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function file_field_is_empty($item, $field) {
  return empty($item['fid']);
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
