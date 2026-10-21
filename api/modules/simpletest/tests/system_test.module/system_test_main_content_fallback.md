# system_test_main_content_fallback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 428–430 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L428-L430)
- **Module/theme:** batch_test

## Signature

```php
function system_test_main_content_fallback()
```

## Documentation

```text
Menu callback to test main content fallback().
```

## Code

```php
function system_test_main_content_fallback() {
  return t('Content to test main content fallback');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
