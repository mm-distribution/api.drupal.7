# system_test_page_build()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 408–423 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L408-L423)
- **Module/theme:** batch_test
- **Implements:** [hook_page_build()](../../../system/system.api.php/hook_page_build.md)

## Signature

```php
function system_test_page_build(&$page)
```

## Documentation

```text
Implements hook_page_build().
```

## Code

```php
function system_test_page_build(&$page) {
  $menu_item = menu_get_item();
  $main_content_display = &drupal_static('system_main_content_added', FALSE);

  if ($menu_item['path'] == 'system-test/main-content-handling') {
    $page['footer'] = drupal_set_page_content();
    $page['footer']['main']['#markup'] = '<div id="system-test-content">' . $page['footer']['main']['#markup'] . '</div>';
  }
  elseif ($menu_item['path'] == 'system-test/main-content-fallback') {
    drupal_set_page_content();
    $main_content_display = FALSE;
  }
  elseif ($menu_item['path'] == 'system-test/main-content-duplication') {
    drupal_set_page_content();
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
