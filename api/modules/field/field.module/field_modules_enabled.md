# field_modules_enabled()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 411–414 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L411-L414)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_modules_enabled()](../../system/system.api.php/hook_modules_enabled.md)

## Signature

```php
function field_modules_enabled($modules)
```

## Documentation

```text
Implements hook_modules_enabled().
```

## Code

```php
function field_modules_enabled($modules) {
  // Refresh the 'active' status of fields.
  field_sync_field_status();
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
