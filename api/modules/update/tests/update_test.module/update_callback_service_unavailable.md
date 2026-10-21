# update_callback_service_unavailable()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 189–192 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L189-L192)
- **Module/theme:** aaa_update_test

## Signature

```php
function update_callback_service_unavailable()
```

## Documentation

```text
Page callback: Displays an Error 503 (Service unavailable) page.

@see update_test_menu()
```

## Code

```php
function update_callback_service_unavailable() {
  drupal_add_http_header('Status', '503 Service unavailable');
  print "503 Service Temporarily Unavailable";
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
