# drupal_schema_field_types()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7422–7429 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7422-L7429)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_schema_field_types($table)
```

## Documentation

```text
Retrieves the type for every field in a table schema.

@param $table
  The name of the table from which to retrieve type information.

@return
  An array of types, keyed by field name.
```

## Code

```php
function drupal_schema_field_types($table) {
  $table_schema = drupal_get_schema($table);
  $field_types = array();
  foreach ($table_schema['fields'] as $field_name => $field_info) {
    $field_types[$field_name] = isset($field_info['type']) ? $field_info['type'] : NULL;
  }
  return $field_types;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
