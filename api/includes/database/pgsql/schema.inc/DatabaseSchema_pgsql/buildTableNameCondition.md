# DatabaseSchema_pgsql::buildTableNameCondition()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 852–854 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L852-L854)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function buildTableNameCondition($table_name, $operator = '=', $add_prefix = TRUE)
```

## Documentation

```text
Build a condition to match a table name against a standard information_schema.

In PostgreSQL "unquoted names are always folded to lower case." The pgsql
driver does not quote table names, so they are therefore always lowercase.

@see https://www.postgresql.org/docs/14/sql-syntax-lexical.html
```

## Code

```php
  protected function buildTableNameCondition($table_name, $operator = '=', $add_prefix = TRUE) {
    return parent::buildTableNameCondition(strtolower($table_name), $operator, $add_prefix);
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
