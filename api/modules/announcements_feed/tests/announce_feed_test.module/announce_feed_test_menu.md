# announce_feed_test_menu()

- **Type:** Function
- **File:** [`modules/announcements_feed/tests/announce_feed_test.module`](_file.md), lines 11–21 · [local source](../../../../../source/modules/announcements_feed/tests/announce_feed_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.module#L11-L21)
- **Module/theme:** announce_feed_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function announce_feed_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function announce_feed_test_menu() {
  $items['announcements-feed-json/%'] = array(
    'title' => 'Announcements feed JSON',
    'page callback' => 'announce_feed_test_set_feed_config',
    'page arguments' => array(1),
    // In unit tests, restrictions are not required.
    'access callback' => TRUE,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
