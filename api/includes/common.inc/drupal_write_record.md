# drupal_write_record()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7485–7617 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7485-L7617)
- **Topics:** [schemaapi](../../topics/schemaapi.md)

## Signature

```php
function drupal_write_record($table, &$record, $primary_keys = array())
```

## Documentation

```text
Saves (inserts or updates) a record to the database based upon the schema.

Do not use drupal_write_record() within hook_update_N() functions, since the
database schema cannot be relied upon when a user is running a series of
updates. Instead, use db_insert() or db_update() to save the record.

@param $table
  The name of the table; this must be defined by a hook_schema()
  implementation.
@param $record
  An object or array representing the record to write, passed in by
  reference. If inserting a new record, values not provided in $record will
  be populated in $record and in the database with the default values from
  the schema, as well as a single serial (auto-increment) field (if present).
  If updating an existing record, only provided values are updated in the
  database, and $record is not modified.
@param $primary_keys
  To indicate that this is a new record to be inserted, omit this argument.
  If this is an update, this argument specifies the primary keys' field
  names. If there is only 1 field in the key, you may pass in a string; if
  there are multiple fields in the key, pass in an array.

@return
  If the record insert or update failed, returns FALSE. If it succeeded,
  returns SAVED_NEW or SAVED_UPDATED, depending on the operation performed.
```

## Code

```php
function drupal_write_record($table, &$record, $primary_keys = array()) {
  // Standardize $primary_keys to an array.
  if (is_string($primary_keys)) {
    $primary_keys = array($primary_keys);
  }

  $schema = drupal_get_schema($table);
  if (empty($schema)) {
    return FALSE;
  }

  $object = (object) $record;
  $fields = array();

  // Go through the schema to determine fields to write.
  foreach ($schema['fields'] as $field => $info) {
    if ($info['type'] == 'serial') {
      // Skip serial types if we are updating.
      if (!empty($primary_keys)) {
        continue;
      }
      // Track serial field so we can helpfully populate them after the query.
      // NOTE: Each table should come with one serial field only.
      $serial = $field;
    }

    // Skip field if it is in $primary_keys as it is unnecessary to update a
    // field to the value it is already set to.
    if (in_array($field, $primary_keys)) {
      continue;
    }

    if (!property_exists($object, $field)) {
      // Skip fields that are not provided, default values are already known
      // by the database.
      continue;
    }

    // Build array of fields to update or insert.
    if (empty($info['serialize'])) {
      $fields[$field] = $object->$field;
    }
    else {
      $fields[$field] = serialize($object->$field);
    }

    // Type cast to proper datatype, except when the value is NULL and the
    // column allows this.
    //
    // MySQL PDO silently casts e.g. FALSE and '' to 0 when inserting the value
    // into an integer column, but PostgreSQL PDO does not. Also type cast NULL
    // when the column does not allow this.
    if (isset($object->$field) || !empty($info['not null'])) {
      if ($info['type'] == 'int' || $info['type'] == 'serial') {
        $fields[$field] = (int) $fields[$field];
      }
      elseif ($info['type'] == 'float') {
        $fields[$field] = (float) $fields[$field];
      }
      else {
        $fields[$field] = (string) $fields[$field];
      }
    }
  }

  if (empty($fields)) {
    return;
  }

  // Build the SQL.
  if (empty($primary_keys)) {
    // We are doing an insert.
    $options = array('return' => Database::RETURN_INSERT_ID);
    if (isset($serial) && isset($fields[$serial])) {
      // If the serial column has been explicitly set with an ID, then we don't
      // require the database to return the last insert id.
      if ($fields[$serial]) {
        $options['return'] = Database::RETURN_AFFECTED;
      }
      // If a serial column does exist with no value (i.e. 0) then remove it as
      // the database will insert the correct value for us.
      else {
        unset($fields[$serial]);
      }
    }
    $query = db_insert($table, $options)->fields($fields);
    $return = SAVED_NEW;
  }
  else {
    $query = db_update($table)->fields($fields);
    foreach ($primary_keys as $key) {
      $query->condition($key, $object->$key);
    }
    $return = SAVED_UPDATED;
  }

  // Execute the SQL.
  if ($query_return = $query->execute()) {
    if (isset($serial)) {
      // If the database was not told to return the last insert id, it will be
      // because we already know it.
      if (isset($options) && $options['return'] != Database::RETURN_INSERT_ID) {
        $object->$serial = $fields[$serial];
      }
      else {
        $object->$serial = $query_return;
      }
    }
  }
  // If we have a single-field primary key but got no insert ID, the
  // query failed. Note that we explicitly check for FALSE, because
  // a valid update query which doesn't change any values will return
  // zero (0) affected rows.
  elseif ($query_return === FALSE && count($primary_keys) == 1) {
    $return = FALSE;
  }

  // If we are inserting, populate empty fields with default values.
  if (empty($primary_keys)) {
    foreach ($schema['fields'] as $field => $info) {
      if (isset($info['default']) && !property_exists($object, $field)) {
        $object->$field = $info['default'];
      }
    }
  }

  // If we began with an array, convert back.
  if (is_array($record)) {
    $record = (array) $object;
  }

  return $return;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
