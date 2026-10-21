# drupal_get_schema_unprocessed()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7361–7373 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7361-L7373)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_get_schema_unprocessed($module, $table = NULL)
```

## Documentation

```text
Returns the unprocessed and unaltered version of a module's schema.

Use this function only if you explicitly need the original
specification of a schema, as it was defined in a module's
hook_schema(). No additional default values will be set,
hook_schema_alter() is not invoked and these unprocessed
definitions won't be cached. To retrieve the schema after
hook_schema_alter() has been invoked use drupal_get_schema().

This function can be used to retrieve a schema specification in
hook_schema(), so it allows you to derive your tables from existing
specifications.

It is also used by drupal_install_schema() and
drupal_uninstall_schema() to ensure that a module's tables are
created exactly as specified without any changes introduced by a
module that implements hook_schema_alter().

@param $module
  The module to which the table belongs.
@param $table
  The name of the table. If not given, the module's complete schema
  is returned.
```

## Code

```php
function drupal_get_schema_unprocessed($module, $table = NULL) {
  // Load the .install file to get hook_schema.
  module_load_install($module);
  $schema = module_invoke($module, 'schema');

  if (isset($table) && isset($schema[$table])) {
    return $schema[$table];
  }
  elseif (!empty($schema)) {
    return $schema;
  }
  return array();
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
