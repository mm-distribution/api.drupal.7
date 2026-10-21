# DatabaseSchema_mysql::buildTableNameCondition()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 57–71 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L57-L71)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
protected function buildTableNameCondition($table_name, $operator = '=', $add_prefix = TRUE)
```

## Documentation

```text
Build a condition to match a table name against a standard information_schema.

MySQL uses databases like schemas rather than catalogs so when we build
a condition to query the information_schema.tables, we set the default
database as the schema unless specified otherwise, and exclude table_catalog
from the condition criteria.
```

## Code

```php
  protected function buildTableNameCondition($table_name, $operator = '=', $add_prefix = TRUE) {
    $info = $this->connection->getConnectionOptions();

    // Ensure the table name is not surrounded with quotes as that is not
    // appropriate for schema queries.
    $quote_char = variable_get('mysql_identifier_quote_character', MYSQL_IDENTIFIER_QUOTE_CHARACTER_DEFAULT);
    $table_name = str_replace($quote_char, '', $table_name);

    $table_info = $this->getPrefixInfo($table_name, $add_prefix);

    $condition = new DatabaseCondition('AND');
    $condition->condition('table_schema', $table_info['database']);
    $condition->condition('table_name', $table_info['table'], $operator);
    return $condition;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
