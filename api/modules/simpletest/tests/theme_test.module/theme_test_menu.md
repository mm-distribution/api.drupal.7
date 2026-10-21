# theme_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 45–77 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L45-L77)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function theme_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function theme_test_menu() {
  $items['theme-test/suggestion'] = array(
    'title' => 'Suggestion',
    'page callback' => '_theme_test_suggestion',
    'access arguments' => array('access content'),
    'theme callback' => '_theme_custom_theme',
    'type' => MENU_CALLBACK,
  );
  $items['theme-test/alter'] = array(
    'title' => 'Suggestion',
    'page callback' => '_theme_test_alter',
    'access arguments' => array('access content'),
    'theme callback' => '_theme_custom_theme',
    'type' => MENU_CALLBACK,
  );
  $items['theme-test/hook-init'] = array(
    'page callback' => 'theme_test_hook_init_page_callback',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['theme-test/drupal-add-region-content'] = array(
    'page callback' => '_theme_test_drupal_add_region_content',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['theme-test/engine-info-test'] = array(
    'description' => "Serves a simple page rendered using a Nyan Cat theme engine template.",
    'page callback' => '_theme_test_engine_info_test',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
