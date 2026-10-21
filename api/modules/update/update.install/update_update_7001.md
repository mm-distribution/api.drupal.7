# update_update_7001()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 181–186 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L181-L186)
- **Module/theme:** update
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function update_update_7001()
```

## Documentation

```text
Recreates cache_update table.

Converts fields that hold serialized variables from text to blob.
Removes 'headers' column.
```

## Code

```php
function update_update_7001() {
  $schema = system_schema_cache_7054();

  db_drop_table('cache_update');
  db_create_table('cache_update', $schema);
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
