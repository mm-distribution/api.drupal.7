# DatabaseSchema_pgsql::processField()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 319–357 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L319-L357)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

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
    // In case one is already provided, force it to lowercase.
    if (isset($field['pgsql_type'])) {
      $field['pgsql_type'] = drupal_strtolower($field['pgsql_type']);
    }
    else {
      $map = $this->getFieldTypeMap();
      $field['pgsql_type'] = $map[$field['type'] . ':' . $field['size']];
    }

    if (!empty($field['unsigned'])) {
      // Unsigned datatypes are not supported in PostgreSQL 8.3. In MySQL,
      // they are used to ensure a positive number is inserted and it also
      // doubles the maximum integer size that can be stored in a field.
      // The PostgreSQL schema in Drupal creates a check constraint
      // to ensure that a value inserted is >= 0. To provide the extra
      // integer capacity, here, we bump up the column field size.
      if (!isset($map)) {
        $map = $this->getFieldTypeMap();
      }
      switch ($field['pgsql_type']) {
        case 'smallint':
          $field['pgsql_type'] = $map['int:medium'];
          break;
        case 'int' :
          $field['pgsql_type'] = $map['int:big'];
          break;
      }
    }
    if (isset($field['type']) && $field['type'] == 'serial') {
      unset($field['not null']);
    }
    return $field;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
