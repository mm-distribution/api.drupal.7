# DatabaseCondition::__clone()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1944–1956 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1944-L1956)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
function __clone()
```

## Documentation

```text
PHP magic __clone() method.

Only copies fields that implement QueryConditionInterface. Also sets
$this->changed to TRUE.
```

## Code

```php
  function __clone() {
    $this->changed = TRUE;
    foreach ($this->conditions as $key => $condition) {
      if ($key !== '#conjunction') {
        if ($condition['field'] instanceOf QueryConditionInterface) {
          $this->conditions[$key]['field'] = clone($condition['field']);
        }
        if ($condition['value'] instanceOf SelectQueryInterface) {
          $this->conditions[$key]['value'] = clone($condition['value']);
        }
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
