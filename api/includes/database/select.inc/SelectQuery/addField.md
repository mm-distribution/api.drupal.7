# SelectQuery::addField()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1319–1345 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1319-L1345)
- **Class:** [SelectQuery](../SelectQuery.md)
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
    // If no alias is specified, first try the field name itself.
    if (empty($alias)) {
      $alias = $field;
    }

    // If that's already in use, try the table name and field name.
    if (!empty($this->fields[$alias])) {
      $alias = $table_alias . '_' . $field;
    }

    // If that is already used, just add a counter until we find an unused alias.
    $alias_candidate = $alias;
    $count = 2;
    while (!empty($this->fields[$alias_candidate])) {
      $alias_candidate = $alias . '_' . $count++;
    }
    $alias = $alias_candidate;

    $this->fields[$alias] = array(
      'field' => $field,
      'table' => $table_alias,
      'alias' => $alias,
    );

    return $alias;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
