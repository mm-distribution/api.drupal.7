# DatabaseSchema::buildTableNameCondition()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 299–310 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L299-L310)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
protected function buildTableNameCondition($table_name, $operator = '=', $add_prefix = TRUE)
```

## Documentation

```text
Build a condition to match a table name against a standard information_schema.

The information_schema is a SQL standard that provides information about the
database server and the databases, schemas, tables, columns and users within
it. This makes information_schema a useful tool to use across the drupal
database drivers and is used by a few different functions. The function below
describes the conditions to be meet when querying information_schema.tables
for drupal tables or information associated with drupal tables. Even though
this is the standard method, not all databases follow standards and so this
method should be overwritten by a database driver if the database provider
uses alternate methods. Because information_schema.tables is used in a few
different functions, a database driver will only need to override this function
to make all the others work. For example see includes/databases/mysql/schema.inc.

@param $table_name
  The name of the table in question.
@param $operator
  The operator to apply on the 'table' part of the condition.
@param $add_prefix
  Boolean to indicate whether the table name needs to be prefixed.

@return QueryConditionInterface
  A DatabaseCondition object.
```

## Code

```php
  protected function buildTableNameCondition($table_name, $operator = '=', $add_prefix = TRUE) {
    $info = $this->connection->getConnectionOptions();

    // Retrieve the table name and schema
    $table_info = $this->getPrefixInfo($table_name, $add_prefix);

    $condition = new DatabaseCondition('AND');
    $condition->condition('table_catalog', $info['database']);
    $condition->condition('table_schema', $table_info['schema']);
    $condition->condition('table_name', $table_info['table'], $operator);
    return $condition;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
