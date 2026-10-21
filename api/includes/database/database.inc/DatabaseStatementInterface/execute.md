# DatabaseStatementInterface::execute()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2082–2082 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2082)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function execute($args = array(), $options = array());
```

## Documentation

```text
Executes a prepared statement

@param $args
  An array of values with as many elements as there are bound parameters in
  the SQL statement being executed.
@param $options
  An array of options for this query.

@return
  TRUE on success, or FALSE on failure.
```

## Code

```php
  public function execute($args = array(), $options = array());
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
