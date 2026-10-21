# SearchQuery::countQuery()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 523–545 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L523-L545)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
public function countQuery()
```

## Documentation

```text
Builds the default count query for SearchQuery.

Since SearchQuery always uses GROUP BY, we can default to a subquery. We
also add the same conditions as execute() because countQuery() is called
first.
```

## Code

```php
  public function countQuery() {
    // Clone the inner query.
    $inner = clone $this->query;

    // Add conditions to query.
    $inner->join('search_dataset', 'd', 'i.sid = d.sid AND i.type = d.type');
    $inner->condition($this->conditions);

    // Remove existing fields and expressions, they are not needed for a count
    // query.
    $fields =& $inner->getFields();
    $fields = array();
    $expressions =& $inner->getExpressions();
    $expressions = array();

    // Add the sid as the only field and count them as a subquery.
    $count = db_select($inner->fields('i', array('sid')), NULL, array('target' => 'slave'));

    // Add the COUNT() expression.
    $count->addExpression('COUNT(*)');

    return $count;
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
