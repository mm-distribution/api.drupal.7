# EntityFieldQuery::tableSort()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1072–1095 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1072-L1095)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function tableSort(&$headers)
```

## Documentation

```text
Enables sortable tables for this query.

@param $headers
  An EFQ Header array based on which the order clause is added to the
  query.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function tableSort(&$headers) {
    // If 'field' is not initialized, the header columns aren't clickable
    foreach ($headers as $key =>$header) {
      if (is_array($header) && isset($header['specifier'])) {
        $headers[$key]['field'] = '';
      }
    }

    $order = tablesort_get_order($headers);
    $direction = tablesort_get_sort($headers);
    foreach ($headers as $header) {
      if (is_array($header) && ($header['data'] == $order['name'])) {
        if ($header['type'] == 'field') {
          $this->fieldOrderBy($header['specifier']['field'], $header['specifier']['column'], $direction);
        }
        else {
          $header['direction'] = $direction;
          $this->order[] = $header;
        }
      }
    }

    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
