# Query::__clone()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 359–361 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L359-L361)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __clone()
```

## Documentation

```text
Implements the magic __clone function.
```

## Code

```php
  public function __clone() {
    $this->uniqueIdentifier = uniqid('', TRUE);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
