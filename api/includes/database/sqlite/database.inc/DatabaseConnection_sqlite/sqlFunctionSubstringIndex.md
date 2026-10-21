# DatabaseConnection_sqlite::sqlFunctionSubstringIndex()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 216–229 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L216-L229)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function sqlFunctionSubstringIndex($string, $delimiter, $count)
```

## Documentation

```text
SQLite compatibility implementation for the SUBSTRING_INDEX() SQL function.
```

## Code

```php
  public function sqlFunctionSubstringIndex($string, $delimiter, $count) {
    // If string is empty, simply return an empty string.
    if (empty($string)) {
      return '';
    }
    $end = 0;
    for ($i = 0; $i < $count; $i++) {
      $end = strpos($string, $delimiter, $end + 1);
      if ($end === FALSE) {
        $end = strlen($string);
      }
    }
    return substr($string, 0, $end);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
