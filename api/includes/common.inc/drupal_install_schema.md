# drupal_install_schema()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7301–7308 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7301-L7308)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_install_schema($module)
```

## Documentation

```text
Creates all tables defined in a module's hook_schema().

Note: This function does not pass the module's schema through
hook_schema_alter(). The module's tables will be created exactly as the
module defines them.

@param $module
  The module for which the tables will be created.
```

## Code

```php
function drupal_install_schema($module) {
  $schema = drupal_get_schema_unprocessed($module);
  _drupal_schema_initialize($schema, $module, FALSE);

  foreach ($schema as $name => $table) {
    db_create_table($name, $table);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
