# aggregator_test_menu()

- **Type:** Function
- **File:** [`modules/aggregator/tests/aggregator_test.module`](_file.md), lines 6–15 · [local source](../../../../../source/modules/aggregator/tests/aggregator_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/tests/aggregator_test.module#L6-L15)
- **Module/theme:** aggregator_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function aggregator_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function aggregator_test_menu() {
  $items['aggregator/test-feed'] = array(
    'title' => 'Test feed static last modified date',
    'description' => "A cached test feed with a static last modified date.",
    'page callback' => 'aggregator_test_feed',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/aggregator/tests/aggregator_test.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/tests/aggregator_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
