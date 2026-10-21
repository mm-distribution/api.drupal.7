# DatabaseSchema_sqlite::changeField()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 495–537 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L495-L537)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function changeField($table, $field, $field_new, $spec, $keys_new = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function changeField($table, $field, $field_new, $spec, $keys_new = array()) {
    if (!$this->fieldExists($table, $field)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot change the definition of field @table.@name: field doesn't exist.", array('@table' => $table, '@name' => $field)));
    }
    if (($field != $field_new) && $this->fieldExists($table, $field_new)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot rename field @table.@name to @name_new: target field already exists.", array('@table' => $table, '@name' => $field, '@name_new' => $field_new)));
    }

    $old_schema = $this->introspectSchema($table);
    $new_schema = $old_schema;

    // Map the old field to the new field.
    if ($field != $field_new) {
      $mapping[$field_new] = $field;
    }
    else {
      $mapping = array();
    }

    // Remove the previous definition and swap in the new one.
    unset($new_schema['fields'][$field]);
    $new_schema['fields'][$field_new] = $spec;

    // Map the former indexes to the new column name.
    $new_schema['primary key'] = $this->mapKeyDefinition($new_schema['primary key'], $mapping);
    foreach (array('unique keys', 'indexes') as $k) {
      foreach ($new_schema[$k] as &$key_definition) {
        $key_definition = $this->mapKeyDefinition($key_definition, $mapping);
      }
    }

    // Add in the keys from $keys_new.
    if (isset($keys_new['primary key'])) {
      $new_schema['primary key'] = $keys_new['primary key'];
    }
    foreach (array('unique keys', 'indexes') as $k) {
      if (!empty($keys_new[$k])) {
        $new_schema[$k] = $keys_new[$k] + $new_schema[$k];
      }
    }

    $this->alterTable($table, $old_schema, $new_schema, $mapping);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
