# field_test_query_efq_table_prefixing_test_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 269–273 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L269-L273)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_query_TAG_alter()](../../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function field_test_query_efq_table_prefixing_test_alter(&$query)
```

## Documentation

```text
Implements hook_query_TAG_alter() for tag 'efq_table_prefixing_test'.

@see EntityFieldQueryTestCase::testTablePrefixing()
```

## Code

```php
function field_test_query_efq_table_prefixing_test_alter(&$query) {
  // Add an additional join onto the entity base table. This will cause an
  // exception if the EFQ does not properly prefix the base table.
  $query->join('test_entity','te2','%alias.ftid = test_entity.ftid');
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
