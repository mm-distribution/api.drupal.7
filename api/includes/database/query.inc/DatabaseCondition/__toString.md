# DatabaseCondition::__toString()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1930–1936 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1930-L1936)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

```text
Implements PHP magic __toString method to convert the conditions to string.

@return string
  A string version of the conditions.
```

## Code

```php
  public function __toString() {
    // If the caller forgot to call compile() first, refuse to run.
    if ($this->changed) {
      return '';
    }
    return $this->stringVersion;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
