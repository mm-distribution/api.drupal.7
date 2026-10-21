# tablesort_get_order()

- **Type:** Function
- **File:** [`includes/tablesort.inc`](_file.md), lines 204–228 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L204-L228)

## Signature

```php
function tablesort_get_order($headers)
```

## Documentation

```text
Determines the current sort criterion.

@param $headers
  An array of column headers in the format described in theme_table().

@return
  An associative array describing the criterion, containing the keys:
  - "name": The localized title of the table column.
  - "sql": The name of the database field to sort on.
```

## Code

```php
function tablesort_get_order($headers) {
  $order = isset($_GET['order']) ? $_GET['order'] : '';
  foreach ($headers as $header) {
    if (is_array($header)) {
      if (isset($header['data']) && $order == $header['data']) {
        $default = $header;
        break;
      }

      if (empty($default) && isset($header['sort']) && ($header['sort'] == 'asc' || $header['sort'] == 'desc')) {
        $default = $header;
      }
    }
  }

  if (!isset($default)) {
    $default = reset($headers);
    if (!is_array($default)) {
      $default = array('data' => $default);
    }
  }

  $default += array('data' => NULL, 'field' => NULL);
  return array('name' => $default['data'], 'sql' => $default['field']);
}
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
