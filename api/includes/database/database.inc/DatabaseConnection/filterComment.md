# DatabaseConnection::filterComment()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 689–691 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L689-L691)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function filterComment($comment = '')
```

## Documentation

```text
Sanitize a query comment string.

Ensure a query comment does not include strings such as "* /" that might
terminate the comment early. This avoids SQL injection attacks via the
query comment. The comment strings in this example are separated by a
space to avoid PHP parse errors.

For example, the comment:
@code
db_update('example')
 ->condition('id', $id)
 ->fields(array('field2' => 10))
 ->comment('Exploit * / DROP TABLE node; --')
 ->execute()
@endcode

Would result in the following SQL statement being generated:
@code
"/ * Exploit * / DROP TABLE node; -- * / UPDATE example SET field2=..."
@endcode

Unless the comment is sanitised first, the SQL server would drop the
node table and ignore the rest of the SQL statement.

@param $comment
  A query comment string.

@return
  A sanitized version of the query comment string.
```

## Code

```php
  protected function filterComment($comment = '') {
    return strtr($comment, array('*' => ' * '));
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
