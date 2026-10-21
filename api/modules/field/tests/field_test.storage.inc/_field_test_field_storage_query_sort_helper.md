# _field_test_field_storage_query_sort_helper()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 248–260 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L248-L260)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function _field_test_field_storage_query_sort_helper($a, $b)
```

## Documentation

```text
Sort helper for field_test_field_storage_query().

Sorts by entity type and entity id.
```

## Code

```php
function _field_test_field_storage_query_sort_helper($a, $b) {
  if ($a->type == $b->type) {
    if ($a->entity_id == $b->entity_id) {
      return 0;
    }
    else {
      return $a->entity_id < $b->entity_id ? -1 : 1;
    }
  }
  else {
    return $a->type < $b->type ? -1 : 1;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
