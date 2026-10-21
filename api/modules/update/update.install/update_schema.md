# update_schema()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 62–66 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L62-L66)
- **Module/theme:** update
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function update_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function update_schema() {
  $schema['cache_update'] = drupal_get_schema_unprocessed('system', 'cache');
  $schema['cache_update']['description'] = 'Cache table for the Update module to store information about available releases, fetched from central server.';
  return $schema;
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
