# locale_test_menu()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 62–71 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L62-L71)
- **Module/theme:** locale_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function locale_test_menu()
```

## Documentation

```text
Implements hook_menu().

@return array
```

## Code

```php
function locale_test_menu() {
  $items = array();
  $items['locale_test_plural_format_page'] = array(
    'page callback' => 'locale_test_plural_format_page',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
