# _list_values_in_use()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 371–382 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L371-L382)
- **Module/theme:** list

## Signature

```php
function _list_values_in_use($field, $values)
```

## Documentation

```text
Checks if a list of values are being used in actual field values.
```

## Code

```php
function _list_values_in_use($field, $values) {
  if ($values) {
    $query = new EntityFieldQuery();
    $found = $query
      ->fieldCondition($field['field_name'], 'value', $values)
      ->range(0, 1)
      ->execute();
    return !empty($found);
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
