# _theme_test_engine_info_test()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 160–164 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L160-L164)
- **Module/theme:** batch_test

## Signature

```php
function _theme_test_engine_info_test()
```

## Documentation

```text
Serves a simple page renderered using a Nyan Cat theme engine template.
```

## Code

```php
function _theme_test_engine_info_test() {
  return array(
    '#markup' => theme('theme_test_template_test'),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
