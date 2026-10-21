# SelectQueryInterface::addExpression()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 237–237 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L237)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addExpression($expression, $alias = NULL, $arguments = array());
```

## Documentation

```text
Adds an expression to the list of "fields" to be SELECTed.

An expression can be any arbitrary string that is valid SQL. That includes
various functions, which may in some cases be database-dependent. This
method makes no effort to correct for database-specific functions.

@param $expression
  The expression string. May contain placeholders.
@param $alias
  The alias for this expression. If not specified, one will be generated
  automatically in the form "expression_#". The alias will be checked for
  uniqueness, so the requested alias may not be the alias that is assigned
  in all cases.
@param $arguments
  Any placeholder arguments needed for this expression.
@return
  The unique alias that was assigned for this expression.
```

## Code

```php
  public function addExpression($expression, $alias = NULL, $arguments = array());
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
