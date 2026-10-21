# field_permission()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 322–332 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L322-L332)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function field_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function field_permission() {
  return array(
    'administer fields' => array(
      'title' => t('Administer fields'),
      'description' => t('Additional permissions are required based on what the fields are attached to (for example, <a href="@url">administer content types</a> to manage fields attached to content).', array(
        '@url' => '#module-node',
      )),
      'restrict access' => TRUE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
