# db_xor()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2800–2802 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2800-L2802)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_xor()
```

## Documentation

```text
Returns a new DatabaseCondition, set to "XOR" all conditions together.

@return DatabaseCondition
```

## Code

```php
function db_xor() {
  return new DatabaseCondition('XOR');
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
