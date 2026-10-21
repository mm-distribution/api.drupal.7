# DatabaseSchema::tableExists()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 321–330 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L321-L330)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function tableExists($table)
```

## Documentation

```text
Check if a table exists.

@param $table
  The name of the table in drupal (no prefixing).

@return
  TRUE if the given table exists, otherwise FALSE.
```

## Code

```php
  public function tableExists($table) {
    $condition = $this->buildTableNameCondition($table);
    $condition->compile($this->connection, $this);
    // Normally, we would heartily discourage the use of string
    // concatenation for conditionals like this however, we
    // couldn't use db_select() here because it would prefix
    // information_schema.tables and the query would fail.
    // Don't use {} around information_schema.tables table.
    return (bool) $this->connection->query("SELECT 1 FROM information_schema.tables WHERE " . (string) $condition, $condition->arguments())->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
