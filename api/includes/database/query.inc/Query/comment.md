# Query::comment()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 413–416 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L413-L416)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function comment($comment)
```

## Documentation

```text
Adds a comment to the query.

By adding a comment to a query, you can more easily find it in your
query log or the list of active queries on an SQL server. This allows
for easier debugging and allows you to more easily find where a query
with a performance problem is being generated.

The comment string will be sanitized to remove * / and other characters
that may terminate the string early so as to avoid SQL injection attacks.

@param $comment
  The comment string to be inserted into the query.

@return Query
  The called object.
```

## Code

```php
  public function comment($comment) {
    $this->comments[] = $comment;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
