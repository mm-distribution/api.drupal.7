# DatabaseSchema_pgsql::changeField()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 703–787 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L703-L787)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function changeField($table, $field, $field_new, $spec, $new_keys = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function changeField($table, $field, $field_new, $spec, $new_keys = array()) {
    if (!$this->fieldExists($table, $field)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot change the definition of field @table.@name: field doesn't exist.", array('@table' => $table, '@name' => $field)));
    }
    if (($field != $field_new) && $this->fieldExists($table, $field_new)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot rename field @table.@name to @name_new: target field already exists.", array('@table' => $table, '@name' => $field, '@name_new' => $field_new)));
    }

    $spec = $this->processField($spec);

    // We need to typecast the new column to best be able to transfer the data
    // Schema_pgsql::getFieldTypeMap() will return possibilities that are not
    // 'cast-able' such as 'serial' - so they need to be casted int instead.
    if (in_array($spec['pgsql_type'], array('serial', 'bigserial', 'numeric'))) {
      $typecast = 'int';
    }
    else {
      $typecast = $spec['pgsql_type'];
    }

    if (in_array($spec['pgsql_type'], array('varchar', 'character', 'text')) && isset($spec['length'])) {
      $typecast .= '(' . $spec['length'] . ')';
    }
    elseif (isset($spec['precision']) && isset($spec['scale'])) {
      $typecast .= '(' . $spec['precision'] . ', ' . $spec['scale'] . ')';
    }

    // Remove old check constraints.
    $field_info = $this->queryFieldInformation($table, $field);

    foreach ($field_info as $check) {
      $this->connection->query('ALTER TABLE {' . $table . '} DROP CONSTRAINT "' . $check . '"');
    }

    // Remove old default.
    $this->fieldSetNoDefault($table, $field);

    $this->connection->query('ALTER TABLE {' . $table . '} ALTER "' . $field . '" TYPE ' . $typecast . ' USING "' . $field . '"::' . $typecast);

    if (isset($spec['not null'])) {
      if ($spec['not null']) {
        $nullaction = 'SET NOT NULL';
      }
      else {
        $nullaction = 'DROP NOT NULL';
      }
      $this->connection->query('ALTER TABLE {' . $table . '} ALTER "' . $field . '" ' . $nullaction);
    }

    if (in_array($spec['pgsql_type'], array('serial', 'bigserial'))) {
      // Type "serial" is known to PostgreSQL, but *only* during table creation,
      // not when altering. Because of that, the sequence needs to be created
      // and initialized by hand.
      $seq = "{" . $table . "}_" . $field_new . "_seq";
      $this->connection->query("CREATE SEQUENCE " . $seq);
      // Set sequence to maximal field value to not conflict with existing
      // entries.
      $this->connection->query("SELECT setval('" . $seq . "', MAX(\"" . $field . '")) FROM {' . $table . "}");
      $this->connection->query('ALTER TABLE {' . $table . '} ALTER "' . $field . '" SET DEFAULT nextval(\'' . $seq . '\')');
    }

    // Rename the column if necessary.
    if ($field != $field_new) {
      $this->connection->query('ALTER TABLE {' . $table . '} RENAME "' . $field . '" TO "' . $field_new . '"');
    }

    // Add unsigned check if necessary.
    if (!empty($spec['unsigned'])) {
      $this->connection->query('ALTER TABLE {' . $table . '} ADD CHECK ("' . $field_new . '" >= 0)');
    }

    // Add default if necessary.
    if (isset($spec['default'])) {
      $this->fieldSetDefault($table, $field_new, $spec['default']);
    }

    // Change description if necessary.
    if (!empty($spec['description'])) {
      $this->connection->query('COMMENT ON COLUMN {' . $table . '}."' . $field_new . '" IS ' . $this->prepareComment($spec['description']));
    }

    if (isset($new_keys)) {
      $this->_createKeys($table, $new_keys);
    }
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
