# DatabaseCondition::__construct()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1727–1729 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1727-L1729)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct($conjunction)
```

## Documentation

```text
Constructs a DataBaseCondition object.

@param string $conjunction
  The operator to use to combine conditions: 'AND' or 'OR'.
```

## Code

```php
  public function __construct($conjunction) {
    $this->conditions['#conjunction'] = $conjunction;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
