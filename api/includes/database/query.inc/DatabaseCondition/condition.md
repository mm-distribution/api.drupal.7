# DatabaseCondition::condition()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1746–1767 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1746-L1767)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function condition($field, $value = NULL, $operator = NULL)
```

## Documentation

```text
Implements QueryConditionInterface::condition().
```

## Code

```php
  public function condition($field, $value = NULL, $operator = NULL) {
    if (!isset($operator)) {
      if (is_array($value)) {
        $operator = 'IN';
      }
      elseif (!isset($value)) {
        $operator = 'IS NULL';
      }
      else {
        $operator = '=';
      }
    }
    $this->conditions[] = array(
      'field' => $field,
      'value' => $value,
      'operator' => $operator,
    );

    $this->changed = TRUE;

    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
