# filter_update_7009()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 468–472 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L468-L472)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7009()
```

## Documentation

```text
Converts fields that store serialized variables from text to blob.
```

## Code

```php
function filter_update_7009() {
  $schema = system_schema_cache_7054();
  db_drop_table('cache_filter');
  db_create_table('cache_filter', $schema);
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
