# DatabaseSchema_sqlite::createFieldSql()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 147–186 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L147-L186)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function createFieldSql($name, $spec)
```

## Documentation

```text
Create an SQL string for a field to be used in table creation or alteration.

Before passing a field out of a schema definition into this function it has
to be processed by db_processField().

@param $name
   Name of the field.
@param $spec
   The field specification, as per the schema data structure format.
```

## Code

```php
  protected function createFieldSql($name, $spec) {
    if (!empty($spec['auto_increment'])) {
      $sql = $name . " INTEGER PRIMARY KEY AUTOINCREMENT";
      if (!empty($spec['unsigned'])) {
        $sql .= ' CHECK (' . $name . '>= 0)';
      }
    }
    else {
      $sql = $name . ' ' . $spec['sqlite_type'];

      if (in_array($spec['sqlite_type'], array('VARCHAR', 'TEXT')) && isset($spec['length'])) {
        $sql .= '(' . $spec['length'] . ')';
      }

      if (isset($spec['not null'])) {
        if ($spec['not null']) {
          $sql .= ' NOT NULL';
        }
        else {
          $sql .= ' NULL';
        }
      }

      if (!empty($spec['unsigned'])) {
        $sql .= ' CHECK (' . $name . '>= 0)';
      }

      if (isset($spec['default'])) {
        if (is_string($spec['default'])) {
          $spec['default'] = "'" . $spec['default'] . "'";
        }
        $sql .= ' DEFAULT ' . $spec['default'];
      }

      if (empty($spec['not null']) && !isset($spec['default'])) {
        $sql .= ' DEFAULT NULL';
      }
    }
    return $sql;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
