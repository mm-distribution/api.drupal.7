# TableSort::init()

- **Type:** Method
- **File:** [`includes/tablesort.inc`](../_file.md), lines 59–64 · [local source](../../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L59-L64)
- **Class:** [TableSort](../TableSort.md)

## Signature

```php
protected function init()
```

## Documentation

```text
Initializes the table sort context.
```

## Code

```php
  protected function init() {
    $ts = $this->order();
    $ts['sort'] = $this->getSort();
    $ts['query'] = $this->getQueryParameters();
    return $ts;
  }
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
