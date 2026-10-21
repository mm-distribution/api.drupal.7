# DatabaseConnection::makeComment()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 647–656 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L647-L656)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function makeComment($comments)
```

## Documentation

```text
Flatten an array of query comments into a single comment string.

The comment string will be sanitized to avoid SQL injection attacks.

@param $comments
  An array of query comment strings.

@return
  A sanitized comment string.
```

## Code

```php
  public function makeComment($comments) {
    if (empty($comments))
      return '';

    // Flatten the array of comments.
    $comment = implode('; ', $comments);

    // Sanitize the comment string so as to avoid SQL injection attacks.
    return '/* ' . $this->filterComment($comment) . ' */ ';
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
