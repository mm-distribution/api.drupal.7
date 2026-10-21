# field_sql_storage_update_7000()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.install`](_file.md), lines 92–100 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install#L92-L100)
- **Module/theme:** field_sql_storage
- **Topics:** [updates-6.x-to-7.x](../../../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function field_sql_storage_update_7000()
```

## Documentation

```text
Field SQL storage update version placeholder.
```

## Code

```php
function field_sql_storage_update_7000() {
  // Some update helper functions (such as
  // _update_7000_field_sql_storage_write()) modify the database directly. They
  // can be used safely only if the database schema matches the field module
  // schema established for Drupal 7.0 (i.e. version 7000). This function exists
  // solely to set the schema version to 7000, so that update functions calling
  // those helpers can do so safely by declaring a dependency on
  // field_sql_storage_update_7000().
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install) · Licensed GPL-2.0-or-later (see LICENSE)._
