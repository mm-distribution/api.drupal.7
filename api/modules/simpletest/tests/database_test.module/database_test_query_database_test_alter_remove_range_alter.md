# database_test_query_database_test_alter_remove_range_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 40–42 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L40-L42)
- **Module/theme:** batch_test
- **Implements:** [hook_query_TAG_alter()](../../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function database_test_query_database_test_alter_remove_range_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Implements hook_query_TAG_alter().

Called by DatabaseTestCase::testAlterRemoveRange.
```

## Code

```php
function database_test_query_database_test_alter_remove_range_alter(QueryAlterableInterface $query) {
  $query->range();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
