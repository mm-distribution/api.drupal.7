# tablesort_cell()

- **Type:** Function
- **File:** [`includes/tablesort.inc`](_file.md), lines 170–180 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L170-L180)

## Signature

```php
function tablesort_cell($cell, $header, $ts, $i)
```

## Documentation

```text
Formats a table cell.

Adds a class attribute to all cells in the currently active column.

@param $cell
  The cell to format.
@param $header
  An array of column headers in the format described in theme_table().
@param $ts
  The current table sort context as returned from tablesort_init().
@param $i
  The index of the cell's table column.

@return
  A properly formatted cell, ready for _theme_table_cell().
```

## Code

```php
function tablesort_cell($cell, $header, $ts, $i) {
  if (isset($header[$i]['data']) && $header[$i]['data'] == $ts['name'] && !empty($header[$i]['field'])) {
    if (is_array($cell)) {
      $cell['class'][] = 'active';
    }
    else {
      $cell = array('data' => $cell, 'class' => array('active'));
    }
  }
  return $cell;
}
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
