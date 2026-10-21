# SelectQueryExtender::addField()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 732–734 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L732-L734)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addField($table_alias, $field, $alias = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function addField($table_alias, $field, $alias = NULL) {
    return $this->query->addField($table_alias, $field, $alias);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
