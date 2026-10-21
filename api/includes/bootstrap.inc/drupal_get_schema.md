# drupal_get_schema()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3360–3379 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3360-L3379)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_get_schema($table = NULL, $rebuild = FALSE)
```

## Documentation

```text
Gets the schema definition of a table, or the whole database schema.

The returned schema will include any modifications made by any
module that implements hook_schema_alter(). To get the schema without
modifications, use drupal_get_schema_unprocessed().


@param $table
  The name of the table. If not given, the schema of all tables is returned.
@param $rebuild
  If true, the schema will be rebuilt instead of retrieved from the cache.
```

## Code

```php
function drupal_get_schema($table = NULL, $rebuild = FALSE) {
  static $schema;

  if ($rebuild || !isset($table)) {
    $schema = drupal_get_complete_schema($rebuild);
  }
  elseif (!isset($schema)) {
    $schema = new SchemaCache();
  }

  if (!isset($table)) {
    return $schema;
  }
  if (isset($schema[$table])) {
    return $schema[$table];
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
