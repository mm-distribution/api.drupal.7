# filter_test_filter_format_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/filter_test.module`](_file.md), lines 18–20 · [local source](../../../../../source/modules/simpletest/tests/filter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module#L18-L20)
- **Module/theme:** batch_test
- **Implements:** [hook_filter_format_update()](../../../filter/filter.api.php/hook_filter_format_update.md)

## Signature

```php
function filter_test_filter_format_update($format)
```

## Documentation

```text
Implements hook_filter_format_update().
```

## Code

```php
function filter_test_filter_format_update($format) {
  drupal_set_message('hook_filter_format_update invoked.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/filter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
