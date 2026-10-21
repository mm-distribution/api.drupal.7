# Query::uniqueIdentifier()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 382–384 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L382-L384)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function uniqueIdentifier()
```

## Documentation

```text
Returns a unique identifier for this object.
```

## Code

```php
  public function uniqueIdentifier() {
    return $this->uniqueIdentifier;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
