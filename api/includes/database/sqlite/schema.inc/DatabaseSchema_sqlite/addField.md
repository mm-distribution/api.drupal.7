# DatabaseSchema_sqlite::addField()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 279–331 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L279-L331)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function addField($table, $field, $specification, $keys_new = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function addField($table, $field, $specification, $keys_new = array()) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot add field @table.@field: table doesn't exist.", array('@field' => $field, '@table' => $table)));
    }
    if ($this->fieldExists($table, $field)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot add field @table.@field: field already exists.", array('@field' => $field, '@table' => $table)));
    }

    // SQLite doesn't have a full-featured ALTER TABLE statement. It only
    // supports adding new fields to a table, in some simple cases. In most
    // cases, we have to create a new table and copy the data over.
    if (empty($keys_new) && (empty($specification['not null']) || isset($specification['default']))) {
      // When we don't have to create new keys and we are not creating a
      // NOT NULL column without a default value, we can use the quicker version.
      $query = 'ALTER TABLE {' . $table . '} ADD ' . $this->createFieldSql($field, $this->processField($specification));
      $this->connection->query($query);

      // Apply the initial value if set.
      if (isset($specification['initial'])) {
        $this->connection->update($table)
          ->fields(array($field => $specification['initial']))
          ->execute();
      }
    }
    else {
      // We cannot add the field directly. Use the slower table alteration
      // method, starting from the old schema.
      $old_schema = $this->introspectSchema($table);
      $new_schema = $old_schema;

      // Add the new field.
      $new_schema['fields'][$field] = $specification;

      // Build the mapping between the old fields and the new fields.
      $mapping = array();
      if (isset($specification['initial'])) {
        // If we have a initial value, copy it over.
        $mapping[$field] = array(
          'expression' => ':newfieldinitial',
          'arguments' => array(':newfieldinitial' => $specification['initial']),
        );
      }
      else {
        // Else use the default of the field.
        $mapping[$field] = NULL;
      }

      // Add the new indexes.
      $new_schema += $keys_new;

      $this->alterTable($table, $old_schema, $new_schema, $mapping);
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
