# Query::getComments()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 433–435 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L433-L435)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getComments()
```

## Documentation

```text
Returns a reference to the comments array for the query.

Because this method returns by reference, alter hooks may edit the comments
array directly to make their changes. If just adding comments, however, the
use of comment() is preferred.

Note that this method must be called by reference as well:
@code
$comments =& $query->getComments();
@endcode

@return
  A reference to the comments array structure.
```

## Code

```php
  public function &getComments() {
    return $this->comments;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
