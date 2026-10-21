# drupal_get_query_parameters()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 417–446 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L417-L446)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_get_query_parameters(array $query = NULL, array $exclude = array('q'), $parent = '')
```

## Documentation

```text
Processes a URL query parameter array to remove unwanted elements.

@param $query
  (optional) An array to be processed. Defaults to $_GET.
@param $exclude
  (optional) A list of $query array keys to remove. Use "parent[child]" to
  exclude nested items. Defaults to array('q').
@param $parent
  Internal use only. Used to build the $query array key for nested items.

@return
  An array containing query parameters, which can be used for url().
```

## Code

```php
function drupal_get_query_parameters(array $query = NULL, array $exclude = array('q'), $parent = '') {
  // Set defaults, if none given.
  if (!isset($query)) {
    $query = $_GET;
  }
  // If $exclude is empty, there is nothing to filter.
  if (empty($exclude)) {
    return $query;
  }
  elseif (!$parent) {
    $exclude = array_flip($exclude);
  }

  $params = array();
  foreach ($query as $key => $value) {
    $string_key = ($parent ? $parent . '[' . $key . ']' : $key);
    if (isset($exclude[$string_key])) {
      continue;
    }

    if (is_array($value)) {
      $params[$key] = drupal_get_query_parameters($value, $exclude, $string_key);
    }
    else {
      $params[$key] = $value;
    }
  }

  return $params;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
