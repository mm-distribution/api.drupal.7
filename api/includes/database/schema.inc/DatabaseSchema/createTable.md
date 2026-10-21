# DatabaseSchema::createTable()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 729–737 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L729-L737)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function createTable($name, $table)
```

## Documentation

```text
Create a new table from a Drupal table definition.

@param $name
  The name of the table to create.
@param $table
  A Schema API table definition array.

@throws DatabaseSchemaObjectExistsException
  If the specified table already exists.
```

## Code

```php
  public function createTable($name, $table) {
    if ($this->tableExists($name)) {
      throw new DatabaseSchemaObjectExistsException(t('Table @name already exists.', array('@name' => $name)));
    }
    $statements = $this->createTableSql($name, $table);
    foreach ($statements as $statement) {
      $this->connection->query($statement);
    }
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
