# field_cron()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 351–358 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L351-L358)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function field_cron()
```

## Documentation

```text
Implements hook_cron().
```

## Code

```php
function field_cron() {
  // Refresh the 'active' status of fields.
  field_sync_field_status();

  // Do a pass of purging on deleted Field API data, if any exists.
  $limit = variable_get('field_purge_batch_size', 10);
  field_purge_batch($limit);
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
