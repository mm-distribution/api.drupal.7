# path_delete()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 466–480 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L466-L480)

## Signature

```php
function path_delete($criteria)
```

## Documentation

```text
Delete a URL alias.

@param $criteria
  A number representing the pid or an array of criteria.
```

## Code

```php
function path_delete($criteria) {
  if (!is_array($criteria)) {
    $criteria = array('pid' => $criteria);
  }
  $path = path_load($criteria);
  if (isset($path['source'])) {
    $query = db_delete('url_alias');
    foreach ($criteria as $field => $value) {
      $query->condition($field, $value);
    }
    $query->execute();
    module_invoke_all('path_delete', $path);
    drupal_clear_path_cache($path['source']);
  }
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
