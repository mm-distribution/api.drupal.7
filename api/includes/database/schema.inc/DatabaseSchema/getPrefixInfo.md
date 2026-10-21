# DatabaseSchema::getPrefixInfo()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 238–260 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L238-L260)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
protected function getPrefixInfo($table = 'default', $add_prefix = TRUE)
```

## Documentation

```text
Get information about the table name and schema from the prefix.

@param
  Name of table to look prefix up for. Defaults to 'default' because thats
  default key for prefix.
@param $add_prefix
  Boolean that indicates whether the given table name should be prefixed.

@return
  A keyed array with information about the schema, table name and prefix.
```

## Code

```php
  protected function getPrefixInfo($table = 'default', $add_prefix = TRUE) {
    $info = array(
      'schema' => $this->defaultSchema,
      'prefix' => $this->connection->tablePrefix($table),
    );
    if ($add_prefix) {
      $table = $info['prefix'] . $table;
    }
    // If the prefix contains a period in it, then that means the prefix also
    // contains a schema reference in which case we will change the schema key
    // to the value before the period in the prefix. Everything after the dot
    // will be prefixed onto the front of the table.
    if (($pos = strpos($table, '.')) !== FALSE) {
      // Grab everything before the period.
      $info['schema'] = substr($table, 0, $pos);
      // Grab everything after the dot.
      $info['table'] = substr($table, ++$pos);
    }
    else {
      $info['table'] = $table;
    }
    return $info;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
