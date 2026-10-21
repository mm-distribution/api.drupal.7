# DatabaseSchema_sqlite::processField()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 114–134 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L114-L134)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function processField($field)
```

## Documentation

```text
Set database-engine specific properties for a field.

@param $field
  A field description array, as specified in the schema documentation.
```

## Code

```php
  protected function processField($field) {
    if (!isset($field['size'])) {
      $field['size'] = 'normal';
    }

    // Set the correct database-engine specific datatype.
    // In case one is already provided, force it to uppercase.
    if (isset($field['sqlite_type'])) {
      $field['sqlite_type'] = drupal_strtoupper($field['sqlite_type']);
    }
    else {
      $map = $this->getFieldTypeMap();
      $field['sqlite_type'] = $map[$field['type'] . ':' . $field['size']];
    }

    if (isset($field['type']) && $field['type'] == 'serial') {
      $field['auto_increment'] = TRUE;
    }

    return $field;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
