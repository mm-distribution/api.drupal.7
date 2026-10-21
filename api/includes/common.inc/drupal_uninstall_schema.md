# drupal_uninstall_schema()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7325–7334 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7325-L7334)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_uninstall_schema($module)
```

## Documentation

```text
Removes all tables defined in a module's hook_schema().

Note: This function does not pass the module's schema through
hook_schema_alter(). The module's tables will be created exactly as the
module defines them.

@param $module
  The module for which the tables will be removed.

@return
  An array of arrays with the following key/value pairs:
   - success: a boolean indicating whether the query succeeded.
   - query: the SQL query(s) executed, passed through check_plain().
```

## Code

```php
function drupal_uninstall_schema($module) {
  $schema = drupal_get_schema_unprocessed($module);
  _drupal_schema_initialize($schema, $module, FALSE);

  foreach ($schema as $table) {
    if (db_table_exists($table['name'])) {
      db_drop_table($table['name']);
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
