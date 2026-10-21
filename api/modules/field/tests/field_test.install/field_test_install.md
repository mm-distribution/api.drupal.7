# field_test_install()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.install`](_file.md), lines 11–17 · [local source](../../../../../source/modules/field/tests/field_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.install#L11-L17)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_install()](../../../system/system.api.php/hook_install.md)

## Signature

```php
function field_test_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function field_test_install() {
  // hook_entity_info_alter() needs to be executed as last.
  db_update('system')
    ->fields(array('weight' => 1))
    ->condition('name', 'field_test')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.install](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
