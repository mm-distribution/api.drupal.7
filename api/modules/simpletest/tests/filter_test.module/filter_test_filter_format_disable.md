# filter_test_filter_format_disable()

- **Type:** Function
- **File:** [`modules/simpletest/tests/filter_test.module`](_file.md), lines 25–27 · [local source](../../../../../source/modules/simpletest/tests/filter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module#L25-L27)
- **Module/theme:** batch_test
- **Implements:** [hook_filter_format_disable()](../../../filter/filter.api.php/hook_filter_format_disable.md)

## Signature

```php
function filter_test_filter_format_disable($format)
```

## Documentation

```text
Implements hook_filter_format_disable().
```

## Code

```php
function filter_test_filter_format_disable($format) {
  drupal_set_message('hook_filter_format_disable invoked.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/filter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
