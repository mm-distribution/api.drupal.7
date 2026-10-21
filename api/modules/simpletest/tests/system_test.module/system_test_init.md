# system_test_init()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 325–330 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L325-L330)
- **Module/theme:** batch_test
- **Implements:** [hook_init()](../../../system/system.api.php/hook_init.md)

## Signature

```php
function system_test_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function system_test_init() {
  // Used by FrontPageTestCase to get the results of drupal_is_front_page().
  if (variable_get('front_page_output', 0) && drupal_is_front_page()) {
    drupal_set_message(t('On front page.'));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
