# db_condition()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2814–2816 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2814-L2816)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_condition($conjunction)
```

## Documentation

```text
Returns a new DatabaseCondition, set to the specified conjunction.

Internal API function call.  The db_and(), db_or(), and db_xor()
functions are preferred.

@param $conjunction
  The conjunction to use for query conditions (AND, OR or XOR).
@return DatabaseCondition
```

## Code

```php
function db_condition($conjunction) {
  return new DatabaseCondition($conjunction);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
