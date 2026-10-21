# db_and()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2791–2793 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2791-L2793)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_and()
```

## Documentation

```text
Returns a new DatabaseCondition, set to "AND" all conditions together.

@return DatabaseCondition
```

## Code

```php
function db_and() {
  return new DatabaseCondition('AND');
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
