# SelectQueryExtender::fields()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 736–739 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L736-L739)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fields($table_alias, array $fields = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function fields($table_alias, array $fields = array()) {
    $this->query->fields($table_alias, $fields);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
