# DatabaseConnection::mapConditionOperator()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1350–1350 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1350)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
abstract public function mapConditionOperator($operator);
```

## Documentation

```text
Gets any special processing requirements for the condition operator.

Some condition types require special processing, such as IN, because
the value data they pass in is not a simple value. This is a simple
overridable lookup function. Database connections should define only
those operators they wish to be handled differently than the default.

@param $operator
  The condition operator, such as "IN", "BETWEEN", etc. Case-sensitive.

@return
  The extra handling directives for the specified operator, or NULL.

@see DatabaseCondition::compile()
```

## Code

```php
  abstract public function mapConditionOperator($operator);
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
