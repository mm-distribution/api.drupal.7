# DatabaseSchema_pgsql::queryTableInformation()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 104–163 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L104-L163)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function queryTableInformation($table)
```

## Documentation

```text
Fetch the list of blobs and sequences used on a table.

We introspect the database to collect the information required by insert
and update queries.

@param $table_name
  The non-prefixed name of the table.
@return
  An object with two member variables:
    - 'blob_fields' that lists all the blob fields in the table.
    - 'sequences' that lists the sequences used in that table.
```

## Code

```php
  public function queryTableInformation($table) {
    // Generate a key to reference this table's information on.
    $key = $this->connection->prefixTables('{' . $table . '}');

    // Take into account that temporary tables are stored in a different schema.
    // \DatabaseConnection::generateTemporaryTableName() sets 'db_temporary_'
    // prefix to all temporary tables.
    if (strpos($key, '.') === FALSE && strpos($table, 'db_temporary_') === FALSE) {
      $key = 'public.' . $key;
    }
    else {
      $key = $this->getTempNamespaceName() . '.' . $key;
    }

    if (!isset($this->tableInformation[$key])) {
      $table_information = (object) array(
        'blob_fields' => array(),
        'sequences' => array(),
      );

      // The bytea columns and sequences for a table can be found in
      // pg_attribute, which is significantly faster than querying the
      // information_schema. The data type of a field can be found by lookup
      // of the attribute ID, and the default value must be extracted from the
      // node tree for the attribute definition instead of the historical
      // human-readable column, adsrc.
      $sql = <<<'EOD'
SELECT pg_attribute.attname AS column_name, format_type(pg_attribute.atttypid, pg_attribute.atttypmod) AS data_type, pg_get_expr(pg_attrdef.adbin, pg_attribute.attrelid) AS column_default
FROM pg_attribute
LEFT JOIN pg_attrdef ON pg_attrdef.adrelid = pg_attribute.attrelid AND pg_attrdef.adnum = pg_attribute.attnum
WHERE pg_attribute.attnum > 0
AND NOT pg_attribute.attisdropped
AND pg_attribute.attrelid = :key::regclass
AND (format_type(pg_attribute.atttypid, pg_attribute.atttypmod) = 'bytea'
OR pg_get_expr(pg_attrdef.adbin, pg_attribute.attrelid) LIKE 'nextval%')
EOD;
      $result = $this->connection->query($sql, array(
        ':key' => $key,
      ));

      if (empty($result)) {
        return $table_information;
      }

      foreach ($result as $column) {
        if ($column->data_type == 'bytea') {
          $table_information->blob_fields[$column->column_name] = TRUE;
        }
        elseif (preg_match("/nextval\('([^']+)'/", $column->column_default, $matches)) {
          // We must know of any sequences in the table structure to help us
          // return the last insert id. If there is more than 1 sequences the
          // first one (index 0 of the sequences array) will be used.
          $table_information->sequences[] = $matches[1];
          $table_information->serial_fields[] = $column->column_name;
        }
      }
      $this->tableInformation[$key] = $table_information;
    }
    return $this->tableInformation[$key];
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
