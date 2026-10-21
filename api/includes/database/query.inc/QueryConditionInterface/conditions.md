# QueryConditionInterface::conditions()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 129–129 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L129)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &conditions();
```

## Documentation

```text
Gets a complete list of all conditions in this conditional clause.

This method returns by reference. That allows alter hooks to access the
data structure directly and manipulate it before it gets compiled.

The data structure that is returned is an indexed array of entries, where
each entry looks like the following:
@code
array(
  'field' => $field,
  'value' => $value,
  'operator' => $operator,
);
@endcode

In the special case that $operator is NULL, the $field is taken as a raw
SQL snippet (possibly containing a function) and $value is an associative
array of placeholders for the snippet.

There will also be a single array entry of #conjunction, which is the
conjunction that will be applied to the array, such as AND.
```

## Code

```php
  public function &conditions();
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
