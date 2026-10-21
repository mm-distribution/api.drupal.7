# DatabaseSchema::prepareComment()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 775–777 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L775-L777)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function prepareComment($comment, $length = NULL)
```

## Documentation

```text
Prepare a table or column comment for database query.

@param $comment
  The comment string to prepare.
@param $length
  Optional upper limit on the returned string length.

@return
  The prepared comment.
```

## Code

```php
  public function prepareComment($comment, $length = NULL) {
    return $this->connection->quote($comment);
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
