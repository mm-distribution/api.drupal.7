# DatabaseSchema_sqlite::createKeySql()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 95–106 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L95-L106)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function createKeySql($fields)
```

## Documentation

```text
Build the SQL expression for keys.
```

## Code

```php
  protected function createKeySql($fields) {
    $return = array();
    foreach ($fields as $field) {
      if (is_array($field)) {
        $return[] = $field[0];
      }
      else {
        $return[] = $field;
      }
    }
    return implode(', ', $return);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
