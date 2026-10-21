# DatabaseSchema_mysql::createKeysSqlHelper()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 302–313 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L302-L313)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
protected function createKeysSqlHelper($fields)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function createKeysSqlHelper($fields) {
    $return = array();
    foreach ($fields as $field) {
      if (is_array($field)) {
        $return[] = '`' . $field[0] . '`(' . $field[1] . ')';
      }
      else {
        $return[] = '`' . $field . '`';
      }
    }
    return implode(', ', $return);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
