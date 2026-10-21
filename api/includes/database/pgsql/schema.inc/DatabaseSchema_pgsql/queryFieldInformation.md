# DatabaseSchema_pgsql::queryFieldInformation()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 191–209 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L191-L209)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function queryFieldInformation($table, $field)
```

## Documentation

```text
Fetch the list of CHECK constraints used on a field.

We introspect the database to collect the information required by field
alteration.

@param $table
  The non-prefixed name of the table.
@param $field
  The name of the field.
@return
  An array of all the checks for the field.
```

## Code

```php
  public function queryFieldInformation($table, $field) {
    $prefixInfo = $this->getPrefixInfo($table, TRUE);

    // Split the key into schema and table for querying.
    $schema = $prefixInfo['schema'];
    $table_name = $prefixInfo['table'];

    $field_information = (object) array(
        'checks' => array(),
    );
    $checks = $this->connection->query("SELECT conname FROM pg_class cl INNER JOIN pg_constraint co ON co.conrelid = cl.oid INNER JOIN pg_attribute attr ON attr.attrelid = cl.oid AND attr.attnum = ANY (co.conkey) INNER JOIN pg_namespace ns ON cl.relnamespace = ns.oid WHERE co.contype = 'c' AND ns.nspname = :schema AND cl.relname = :table AND attr.attname = :column", array(
      ':schema' => $schema,
      ':table' => $table_name,
      ':column' => $field,
    ));
    $field_information = $checks->fetchCol();

    return $field_information;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
