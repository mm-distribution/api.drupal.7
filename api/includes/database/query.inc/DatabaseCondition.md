# DatabaseCondition

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 1683–2006 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1683-L2006)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseCondition implements QueryConditionInterface, Countable
```

## Documentation

```text
Generic class for a series of conditions in a query.
```

## Properties

### $conditions

```php
protected $conditions = array();
```

```text
Array of conditions.

@var array
```

### $arguments

```php
protected $arguments = array();
```

```text
Array of arguments.

@var array
```

### $changed

```php
protected $changed = TRUE;
```

```text
Whether the conditions have been changed.

TRUE if the condition has been changed since the last compile.
FALSE if the condition has been compiled and not changed.

@var bool
```

### $queryPlaceholderIdentifier

```php
protected $queryPlaceholderIdentifier;
```

```text
The identifier of the query placeholder this condition has been compiled against.
```

### $stringVersion

```php
protected $stringVersion;
```

```text
Contains the string version of the Condition.

@var string
```

## Methods (derived index)

- [__construct()](DatabaseCondition/__construct.md) — Constructs a DataBaseCondition object.
- [count()](DatabaseCondition/count.md)
- [condition()](DatabaseCondition/condition.md) — Implements QueryConditionInterface::condition().
- [where()](DatabaseCondition/where.md) — Implements QueryConditionInterface::where().
- [isNull()](DatabaseCondition/isNull.md) — Implements QueryConditionInterface::isNull().
- [isNotNull()](DatabaseCondition/isNotNull.md) — Implements QueryConditionInterface::isNotNull().
- [exists()](DatabaseCondition/exists.md) — Implements QueryConditionInterface::exists().
- [notExists()](DatabaseCondition/notExists.md) — Implements QueryConditionInterface::notExists().
- [conditions()](DatabaseCondition/conditions.md) — Implements QueryConditionInterface::conditions().
- [arguments()](DatabaseCondition/arguments.md) — Implements QueryConditionInterface::arguments().
- [compile()](DatabaseCondition/compile.md) — Implements QueryConditionInterface::compile().
- [compiled()](DatabaseCondition/compiled.md) — Implements QueryConditionInterface::compiled().
- [__toString()](DatabaseCondition/__toString.md) — Implements PHP magic __toString method to convert the conditions to string.
- [__clone()](DatabaseCondition/__clone.md) — PHP magic __clone() method.
- [mapConditionOperator()](DatabaseCondition/mapConditionOperator.md) — Gets any special processing requirements for the condition operator.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
