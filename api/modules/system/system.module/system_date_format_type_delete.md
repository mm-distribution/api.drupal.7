# system_date_format_type_delete()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3932–3942 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3932-L3942)
- **Module/theme:** system

## Signature

```php
function system_date_format_type_delete($type)
```

## Documentation

```text
Deletes a date type from the database.

@param $type
  The machine-readable name of the date type.
```

## Code

```php
function system_date_format_type_delete($type) {
  db_delete('date_formats')
    ->condition('type', $type)
    ->execute();
  db_delete('date_format_type')
    ->condition('type', $type)
    ->execute();
  db_delete('date_format_locale')
    ->condition('type', $type)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
