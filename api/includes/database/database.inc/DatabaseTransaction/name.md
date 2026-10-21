# DatabaseTransaction::name()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2027–2029 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2027-L2029)
- **Class:** [DatabaseTransaction](../DatabaseTransaction.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function name()
```

## Documentation

```text
Retrieves the name of the transaction or savepoint.
```

## Code

```php
  public function name() {
    return $this->name;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
