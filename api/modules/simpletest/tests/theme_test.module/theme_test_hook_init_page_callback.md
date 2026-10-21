# theme_test_hook_init_page_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 118–120 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L118-L120)
- **Module/theme:** batch_test

## Signature

```php
function theme_test_hook_init_page_callback()
```

## Documentation

```text
Menu callback for testing themed output generated in hook_init().
```

## Code

```php
function theme_test_hook_init_page_callback() {
  return $GLOBALS['theme_test_output'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
