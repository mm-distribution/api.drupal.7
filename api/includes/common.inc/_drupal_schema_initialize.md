# _drupal_schema_initialize()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7388–7411 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7388-L7411)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function _drupal_schema_initialize(&$schema, $module, $remove_descriptions = TRUE)
```

## Documentation

```text
Fills in required default values for table definitions from hook_schema().

@param $schema
  The schema definition array as it was returned by the module's
  hook_schema().
@param $module
  The module for which hook_schema() was invoked.
@param $remove_descriptions
  (optional) Whether to additionally remove 'description' keys of all tables
  and fields to improve performance of serialize() and unserialize().
  Defaults to TRUE.
```

## Code

```php
function _drupal_schema_initialize(&$schema, $module, $remove_descriptions = TRUE) {
  // Set the name and module key for all tables.
  foreach ($schema as $name => &$table) {
    if (empty($table['module'])) {
      $table['module'] = $module;
    }
    if (!isset($table['name'])) {
      $table['name'] = $name;
    }
    if ($remove_descriptions) {
      unset($table['description']);
      foreach ($table['fields'] as &$field) {
        unset($field['description']);
      }
    }
    // Set the type key for all fields where it is not set (mostly when using
    // datatabase specific data types).
    foreach ($table['fields'] as &$field) {
      if (!isset($field['type'])) {
        $field['type'] = NULL;
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
