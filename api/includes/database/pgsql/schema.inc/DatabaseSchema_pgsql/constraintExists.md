# DatabaseSchema_pgsql::constraintExists()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 627–641 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L627-L641)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function constraintExists($table, $name)
```

## Documentation

```text
Helper function: check if a constraint (PK, FK, UK) exists.

@param $table
  The name of the table.
@param $name
  The name of the constraint (typically 'pkey' or '[constraint]_key').
```

## Code

```php
  protected function constraintExists($table, $name) {
    // ensureIdentifiersLength() expects three parameters, thus we split our
    // constraint name in a proper name and a suffix.
    if ($name == 'pkey') {
      $suffix = $name;
      $name = '';
    }
    else {
      $pos = strrpos($name, '_');
      $suffix = substr($name, $pos + 1);
      $name = substr($name, 0, $pos);
    }
    $constraint_name = $this->ensureIdentifiersLength($table, $name, $suffix);
    return (bool) $this->connection->query("SELECT 1 FROM pg_constraint WHERE conname = '$constraint_name'")->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
