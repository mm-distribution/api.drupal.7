# field_test_query_store_global_test_query_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 278–284 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L278-L284)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_query_TAG_alter()](../../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function field_test_query_store_global_test_query_alter($query)
```

## Documentation

```text
Implements hook_query_TAG_alter() for tag 'store_global_test_query'.
```

## Code

```php
function field_test_query_store_global_test_query_alter($query) {
  // Save the query in a global variable so that it can be examined by tests.
  // This can be used by any test which needs to check a query, but see
  // FieldSqlStorageTestCase::testFieldSqlStorageMultipleConditionsSameColumn()
  // for an example.
  $GLOBALS['test_query'] = $query;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
