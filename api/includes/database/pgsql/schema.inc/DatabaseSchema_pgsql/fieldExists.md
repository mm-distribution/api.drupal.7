# DatabaseSchema_pgsql::fieldExists()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 605–611 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L605-L611)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function fieldExists($table, $column)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function fieldExists($table, $column) {
    // In PostgreSQL "unquoted names are always folded to lower case."
    // @see DatabaseSchema_pgsql::buildTableNameCondition().
    $prefixInfo = $this->getPrefixInfo(strtolower($table));

    return (bool) $this->connection->query("SELECT 1 FROM pg_attribute WHERE attrelid = :key::regclass AND attname = :column AND NOT attisdropped AND attnum > 0", array(':key' => $prefixInfo['schema'] . '.' . $prefixInfo['table'], ':column' => $column))->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
