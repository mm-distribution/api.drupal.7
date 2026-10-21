# DatabaseSchema_sqlite::findTables()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 674–685 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L674-L685)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function findTables($table_expression)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function findTables($table_expression) {
    // Don't add the prefix, $table_expression already includes the prefix.
    $info = $this->getPrefixInfo($table_expression, FALSE);

    // Can't use query placeholders for the schema because the query would have
    // to be :prefixsqlite_master, which does not work.
    $result = db_query("SELECT name FROM " . $info['schema'] . ".sqlite_master WHERE type = :type AND name LIKE :table_name", array(
      ':type' => 'table',
      ':table_name' => $info['table'],
    ));
    return $result->fetchAllKeyed(0, 0);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
