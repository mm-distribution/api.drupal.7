# system_test_page_cache_headers()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 252–269 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L252-L269)
- **Module/theme:** batch_test

## Signature

```php
function system_test_page_cache_headers()
```

## Documentation

```text
Menu callback to test headers stored in the page cache.
```

## Code

```php
function system_test_page_cache_headers() {
  if (!isset($_GET['return_headers'])) {
    return t('Content to store in the page cache if it is enabled.');
  }
  global $base_root;
  // Remove the test query param but try to preserve any remaining query string.
  $url = parse_url($base_root . request_uri());
  $query_parts = explode('&', $url['query']);
  $query_string = implode('&', array_diff($query_parts, array('return_headers=TRUE')));
  $request_uri = $url['path'] . '?' . $query_string;
  $cache = cache_get($base_root . $request_uri, 'cache_page');
  // If there are any headers stored in the cache, output them.
  if (isset($cache->data['headers'])) {
    drupal_add_http_header('Page-Cache-Headers', json_encode($cache->data['headers']));
    return 'Headers from cache_page returned in the Page-Cache-Headers http response header.';
  }
  return 'No headers retrieved from cache_page.';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
