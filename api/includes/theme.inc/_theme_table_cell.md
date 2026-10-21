# _theme_table_cell()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2435–2461 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2435-L2461)

## Signature

```php
function _theme_table_cell($cell, $header = FALSE)
```

## Documentation

```text
Returns HTML output for a single table cell for theme_table().

@param $cell
  Array of cell information, or string to display in cell.
@param bool $header
  TRUE if this cell is a table header cell, FALSE if it is an ordinary
  table cell. If $cell is an array with element 'header' set to TRUE, that
  will override the $header parameter.

@return
  HTML for the cell.
```

## Code

```php
function _theme_table_cell($cell, $header = FALSE) {
  $attributes = '';

  if (is_array($cell)) {
    $data = isset($cell['data']) ? $cell['data'] : '';
    // Cell's data property can be a string or a renderable array.
    if (is_array($data)) {
      $data = drupal_render($data);
    }
    $header |= isset($cell['header']);
    unset($cell['data']);
    unset($cell['header']);
    $attributes = drupal_attributes($cell);
  }
  else {
    $data = $cell;
  }

  if ($header) {
    $output = "<th$attributes>$data</th>";
  }
  else {
    $output = "<td$attributes>$data</td>";
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
