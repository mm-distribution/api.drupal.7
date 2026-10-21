# DatabaseSchema_mysql::prepareComment()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 480–491 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L480-L491)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
public function prepareComment($comment, $length = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function prepareComment($comment, $length = NULL) {
    // Work around a bug in some versions of PDO, see http://bugs.php.net/bug.php?id=41125
    $comment = str_replace("'", '’', $comment);

    // Truncate comment to maximum comment length.
    if (isset($length)) {
      // Add table prefixes before truncating.
      $comment = truncate_utf8($this->connection->prefixTables($comment), $length, TRUE, TRUE);
    }

    return $this->connection->quote($comment);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
