# drupal_schema_fields_sql()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7443–7456 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7443-L7456)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_schema_fields_sql($table, $prefix = NULL)
```

## Documentation

```text
Retrieves a list of fields from a table schema.

The returned list is suitable for use in an SQL query.

@param $table
  The name of the table from which to retrieve fields.
@param
  An optional prefix to to all fields.

@return An array of fields.
```

## Code

```php
function drupal_schema_fields_sql($table, $prefix = NULL) {
  $schema = drupal_get_schema($table);
  $fields = array_keys($schema['fields']);
  if ($prefix) {
    $columns = array();
    foreach ($fields as $field) {
      $columns[] = "$prefix.$field";
    }
    return $columns;
  }
  else {
    return $fields;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
