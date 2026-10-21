# theme_test_init()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 82–94 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L82-L94)
- **Module/theme:** batch_test
- **Implements:** [hook_init()](../../../system/system.api.php/hook_init.md)

## Signature

```php
function theme_test_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function theme_test_init() {
  if (arg(0) == 'theme-test' && arg(1) == 'hook-init') {
    // First, force the theme registry to be rebuilt on this page request. This
    // allows us to test a full initialization of the theme system in the code
    // below.
    drupal_theme_rebuild();
    // Next, initialize the theme system by storing themed text in a global
    // variable. We will use this later in theme_test_hook_init_page_callback()
    // to test that even when the theme system is initialized this early, it is
    // still capable of returning output and theming the page as a whole.
    $GLOBALS['theme_test_output'] = theme('more_link', array('url' => 'user', 'title' => 'Themed output generated in hook_init()'));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
