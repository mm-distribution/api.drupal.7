# hook_filter_format_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 304–306 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L304-L306)
- **Module/theme:** filter
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_filter_format_update($format)
```

## Documentation

```text
Perform actions when a text format has been updated.

This hook allows modules to act when a text format has been updated in any
way. For example, when filters have been reconfigured, disabled, or
re-arranged in the text format.

@param $format
  The format object of the format being updated.

@see hook_filter_format_insert()
@see hook_filter_format_disable()
```

## Code

```php
function hook_filter_format_update($format) {
  mymodule_cache_rebuild();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_filter_format_update()".

- [filter_test_filter_format_update()](../../simpletest/tests/filter_test.module/filter_test_filter_format_update.md) — `modules/simpletest/tests/filter_test.module`
- [text_filter_format_update()](../../field/modules/text/text.module/text_filter_format_update.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
