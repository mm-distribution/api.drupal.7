# DatabaseSchema_pgsql::tableExists()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 420–426 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L420-L426)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function tableExists($table)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function tableExists($table) {
    // In PostgreSQL "unquoted names are always folded to lower case."
    // @see DatabaseSchema_pgsql::buildTableNameCondition().
    $prefixInfo = $this->getPrefixInfo(strtolower($table), TRUE);

    return (bool) $this->connection->query("SELECT 1 FROM pg_tables WHERE schemaname = :schema AND tablename = :table", array(':schema' => $prefixInfo['schema'], ':table' => $prefixInfo['table']))->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
