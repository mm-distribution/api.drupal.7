# url_alter_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/url_alter_test.module`](_file.md), lines 11–19 · [local source](../../../../../source/modules/simpletest/tests/url_alter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module#L11-L19)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function url_alter_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function url_alter_test_menu() {
  $items['url-alter-test/foo'] = array(
    'title' => 'Foo',
    'page callback' => 'url_alter_test_foo',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/url_alter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
