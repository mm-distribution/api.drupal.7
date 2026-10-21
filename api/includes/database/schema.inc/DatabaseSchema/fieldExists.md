# DatabaseSchema::fieldExists()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 428–438 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L428-L438)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function fieldExists($table, $column)
```

## Documentation

```text
Check if a column exists in the given table.

@param $table
  The name of the table in drupal (no prefixing).
@param $name
  The name of the column.

@return
  TRUE if the given column exists, otherwise FALSE.
```

## Code

```php
  public function fieldExists($table, $column) {
    $condition = $this->buildTableNameCondition($table);
    $condition->condition('column_name', $column);
    $condition->compile($this->connection, $this);
    // Normally, we would heartily discourage the use of string
    // concatenation for conditionals like this however, we
    // couldn't use db_select() here because it would prefix
    // information_schema.tables and the query would fail.
    // Don't use {} around information_schema.columns table.
    return (bool) $this->connection->query("SELECT 1 FROM information_schema.columns WHERE " . (string) $condition, $condition->arguments())->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
