# DatabaseSchema_mysql::createTableSql()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 83–131 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L83-L131)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
protected function createTableSql($name, $table)
```

## Documentation

```text
Generate SQL to create a new table from a Drupal schema definition.

@param $name
  The name of the table to create.
@param $table
  A Schema API table definition array.
@return
  An array of SQL statements to create the table.
```

## Code

```php
  protected function createTableSql($name, $table) {
    $info = $this->connection->getConnectionOptions();

    // Provide defaults if needed.
    $table += array(
      'mysql_engine' => 'InnoDB',
      // Allow the default charset to be overridden in settings.php.
      'mysql_character_set' => $this->connection->utf8mb4IsActive() ? 'utf8mb4' : 'utf8',
    );

    $sql = "CREATE TABLE {" . $name . "} (\n";

    // Add the SQL statement for each field.
    foreach ($table['fields'] as $field_name => $field) {
      $sql .= $this->createFieldSql($field_name, $this->processField($field)) . ", \n";
    }

    // Process keys & indexes.
    $keys = $this->createKeysSql($table);
    if (count($keys)) {
      $sql .= implode(", \n", $keys) . ", \n";
    }

    // Remove the last comma and space.
    $sql = substr($sql, 0, -3) . "\n) ";

    $sql .= 'ENGINE = ' . $table['mysql_engine'] . ' DEFAULT CHARACTER SET ' . $table['mysql_character_set'];
    // By default, MySQL uses the default collation for new tables, which is
    // 'utf8_general_ci' for utf8. If an alternate collation has been set, it
    // needs to be explicitly specified.
    // @see DatabaseConnection_mysql
    if (!empty($info['collation'])) {
      $sql .= ' COLLATE ' . $info['collation'];
    }

    // The row format needs to be either DYNAMIC or COMPRESSED in order to allow
    // for the innodb_large_prefix setting to take effect, see
    // https://dev.mysql.com/doc/refman/5.6/en/create-table.html
    if ($this->connection->utf8mb4IsActive()) {
      $sql .= ' ROW_FORMAT=DYNAMIC';
    }

    // Add table comment.
    if (!empty($table['description'])) {
      $sql .= ' COMMENT ' . $this->prepareComment($table['description'], self::COMMENT_MAX_TABLE);
    }

    return array($sql);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
