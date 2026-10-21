# system_date_format_delete()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4007–4011 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4007-L4011)
- **Module/theme:** system

## Signature

```php
function system_date_format_delete($dfid)
```

## Documentation

```text
Deletes a date format from the database.

@param $dfid
  The date format ID.
```

## Code

```php
function system_date_format_delete($dfid) {
  db_delete('date_formats')
    ->condition('dfid', $dfid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
