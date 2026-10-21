# drupal_page_is_cacheable()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1385–1393 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1385-L1393)

## Signature

```php
function drupal_page_is_cacheable($allow_caching = NULL)
```

## Documentation

```text
Determines the cacheability of the current page.

@param $allow_caching
  Set to FALSE if you want to prevent this page from being cached.

@return
  TRUE if the current page can be cached, FALSE otherwise.
```

## Code

```php
function drupal_page_is_cacheable($allow_caching = NULL) {
  $allow_caching_static = &drupal_static(__FUNCTION__, TRUE);
  if (isset($allow_caching)) {
    $allow_caching_static = $allow_caching;
  }

  return $allow_caching_static && ($_SERVER['REQUEST_METHOD'] == 'GET' || $_SERVER['REQUEST_METHOD'] == 'HEAD')
    && !drupal_is_cli();
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
