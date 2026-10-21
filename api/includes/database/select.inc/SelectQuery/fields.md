# SelectQuery::fields()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1347–1361 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1347-L1361)
- **Class:** [SelectQuery](../SelectQuery.md)
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

    if ($fields) {
      foreach ($fields as $field) {
        // We don't care what alias was assigned.
        $this->addField($table_alias, $field);
      }
    }
    else {
      // We want all fields from this table.
      $this->tables[$table_alias]['all_fields'] = TRUE;
    }

    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
