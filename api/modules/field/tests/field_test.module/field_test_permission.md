# field_test_permission()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 23–35 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L23-L35)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_permission()](../../../system/system.api.php/hook_permission.md)

## Signature

```php
function field_test_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function field_test_permission() {
  $perms = array(
    'access field_test content' => array(
      'title' => t('Access field_test content'),
      'description' => t('View published field_test content.'),
    ),
    'administer field_test content' => array(
      'title' => t('Administer field_test content'),
      'description' => t('Manage field_test content'),
    ),
  );
  return $perms;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
