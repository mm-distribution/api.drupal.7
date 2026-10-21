# DatabaseSchema_pgsql::createFieldSql()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 279–311 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L279-L311)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function createFieldSql($name, $spec)
```

## Documentation

```text
Create an SQL string for a field to be used in table creation or
alteration.

Before passing a field out of a schema definition into this
function it has to be processed by _db_process_field().

@param $name
   Name of the field.
@param $spec
   The field specification, as per the schema data structure format.
```

## Code

```php
  protected function createFieldSql($name, $spec) {
    $sql = $name . ' ' . $spec['pgsql_type'];

    if (isset($spec['type']) && $spec['type'] == 'serial') {
      unset($spec['not null']);
    }

    if (in_array($spec['pgsql_type'], array('varchar', 'character', 'text')) && isset($spec['length'])) {
      $sql .= '(' . $spec['length'] . ')';
    }
    elseif (isset($spec['precision']) && isset($spec['scale'])) {
      $sql .= '(' . $spec['precision'] . ', ' . $spec['scale'] . ')';
    }

    if (!empty($spec['unsigned'])) {
      $sql .= " CHECK ($name >= 0)";
    }

    if (isset($spec['not null'])) {
      if ($spec['not null']) {
        $sql .= ' NOT NULL';
      }
      else {
        $sql .= ' NULL';
      }
    }
    if (isset($spec['default'])) {
      $default = is_string($spec['default']) ? "'" . $spec['default'] . "'" : $spec['default'];
      $sql .= " default $default";
    }

    return $sql;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
