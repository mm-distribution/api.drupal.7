# TableSort::orderByHeader()

- **Type:** Method
- **File:** [`includes/tablesort.inc`](../_file.md), lines 42–54 · [local source](../../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L42-L54)
- **Class:** [TableSort](../TableSort.md)

## Signature

```php
public function orderByHeader(Array $header)
```

## Documentation

```text
Order the query based on a header array.

@see theme_table()
@param $header
  Table header array.
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function orderByHeader(Array $header) {
    $this->header = $header;
    $ts = $this->init();
    if (!empty($ts['sql'])) {
      // Based on code from db_escape_table(), but this can also contain a dot.
      $field = preg_replace('/[^A-Za-z0-9_.]+/', '', $ts['sql']);

      // orderBy() will ensure that only ASC/DESC values are accepted, so we
      // don't need to sanitize that here.
      $this->orderBy($field, $ts['sort']);
    }
    return $this;
  }
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
