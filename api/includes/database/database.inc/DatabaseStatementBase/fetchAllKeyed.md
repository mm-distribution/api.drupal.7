# DatabaseStatementBase::fetchAllKeyed()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2321–2328 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2321-L2328)
- **Class:** [DatabaseStatementBase](../DatabaseStatementBase.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAllKeyed($key_index = 0, $value_index = 1)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchAllKeyed($key_index = 0, $value_index = 1) {
    $return = array();
    $this->setFetchMode(PDO::FETCH_NUM);
    foreach ($this as $record) {
      $return[$record[$key_index]] = $record[$value_index];
    }
    return $return;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
