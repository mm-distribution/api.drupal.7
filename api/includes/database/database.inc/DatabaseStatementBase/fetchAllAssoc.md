# DatabaseStatementBase::fetchAllAssoc()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2302–2319 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2302-L2319)
- **Class:** [DatabaseStatementBase](../DatabaseStatementBase.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAllAssoc($key, $fetch = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchAllAssoc($key, $fetch = NULL) {
    $return = array();
    if (isset($fetch)) {
      if (is_string($fetch)) {
        $this->setFetchMode(PDO::FETCH_CLASS, $fetch);
      }
      else {
        $this->setFetchMode($fetch);
      }
    }

    foreach ($this as $record) {
      $record_key = is_object($record) ? $record->$key : $record[$key];
      $return[$record_key] = $record;
    }

    return $return;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
