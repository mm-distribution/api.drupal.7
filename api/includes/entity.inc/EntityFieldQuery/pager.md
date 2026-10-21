# EntityFieldQuery::pager()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1047–1060 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1047-L1060)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function pager($limit = 10, $element = NULL)
```

## Documentation

```text
Enables a pager for the query.

@param $limit
  An integer specifying the number of elements per page.  If passed a false
  value (FALSE, 0, NULL), the pager is disabled.
@param $element
  An optional integer to distinguish between multiple pagers on one page.
  If not provided, one is automatically calculated.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function pager($limit = 10, $element = NULL) {
    if (!isset($element)) {
      $element = PagerDefault::$maxElement++;
    }
    elseif ($element >= PagerDefault::$maxElement) {
      PagerDefault::$maxElement = $element + 1;
    }

    $this->pager = array(
      'limit' => $limit,
      'element' => $element,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
