# DatabaseSchema::findTables()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 342–352 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L342-L352)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function findTables($table_expression)
```

## Documentation

```text
Find all tables that are like the specified base table name.

@param $table_expression
  An SQL expression, for example "simpletest%" (without the quotes).
  BEWARE: this is not prefixed, the caller should take care of that.

@return
  Array, both the keys and the values are the matching tables.
```

## Code

```php
  public function findTables($table_expression) {
    $condition = $this->buildTableNameCondition($table_expression, 'LIKE', FALSE);

    $condition->compile($this->connection, $this);
    // Normally, we would heartily discourage the use of string
    // concatenation for conditionals like this however, we
    // couldn't use db_select() here because it would prefix
    // information_schema.tables and the query would fail.
    // Don't use {} around information_schema.tables table.
    return $this->connection->query("SELECT table_name AS table_name FROM information_schema.tables WHERE " . (string) $condition, $condition->arguments())->fetchAllKeyed(0, 0);
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
