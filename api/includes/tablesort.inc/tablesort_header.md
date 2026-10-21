# tablesort_header()

- **Type:** Function
- **File:** [`includes/tablesort.inc`](_file.md), lines 132–151 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L132-L151)

## Signature

```php
function tablesort_header($cell, $header, $ts)
```

## Documentation

```text
Formats a column header.

If the cell in question is the column header for the current sort criterion,
it gets special formatting. All possible sort criteria become links.

@param $cell
  The cell to format.
@param $header
  An array of column headers in the format described in theme_table().
@param $ts
  The current table sort context as returned from tablesort_init().

@return
  A properly formatted cell, ready for _theme_table_cell().
```

## Code

```php
function tablesort_header($cell, $header, $ts) {
  // Special formatting for the currently sorted column header.
  if (is_array($cell) && isset($cell['field'])) {
    $title = t('sort by @s', array('@s' => $cell['data']));
    if ($cell['data'] == $ts['name']) {
      $ts['sort'] = (($ts['sort'] == 'asc') ? 'desc' : 'asc');
      $cell['class'][] = 'active';
      $image = theme('tablesort_indicator', array('style' => $ts['sort']));
    }
    else {
      // If the user clicks a different header, we want to sort ascending initially.
      $ts['sort'] = 'asc';
      $image = '';
    }
    $cell['data'] = l($cell['data'] . $image, $_GET['q'], array('attributes' => array('title' => $title), 'query' => array_merge($ts['query'], array('sort' => $ts['sort'], 'order' => $cell['data'])), 'html' => TRUE));

    unset($cell['field'], $cell['sort']);
  }
  return $cell;
}
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
