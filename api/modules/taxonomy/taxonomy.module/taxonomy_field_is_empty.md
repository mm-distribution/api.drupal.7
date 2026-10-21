# taxonomy_field_is_empty()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1563–1568 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1563-L1568)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_is_empty()](../../field/field.api.php/hook_field_is_empty.md)

## Signature

```php
function taxonomy_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function taxonomy_field_is_empty($item, $field) {
  if (!is_array($item) || (empty($item['tid']) && (string) $item['tid'] !== '0')) {
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
