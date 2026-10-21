# field_test_dummy_field_storage_query()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 197–204 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L197-L204)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_dummy_field_storage_query(EntityFieldQuery $query)
```

## Documentation

```text
Pseudo-implements hook_field_storage_query().
```

## Code

```php
function field_test_dummy_field_storage_query(EntityFieldQuery $query) {
  // Return dummy values that will be checked by the test.
  return array(
    'user' => array(
      1 => entity_create_stub_entity('user', array(1, NULL, NULL)),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
