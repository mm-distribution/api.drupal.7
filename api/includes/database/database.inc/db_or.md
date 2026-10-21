# db_or()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2782–2784 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2782-L2784)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_or()
```

## Documentation

```text
Returns a new DatabaseCondition, set to "OR" all conditions together.

@return DatabaseCondition
```

## Code

```php
function db_or() {
  return new DatabaseCondition('OR');
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
