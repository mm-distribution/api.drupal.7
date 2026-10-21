# hook_filter_format_disable()

- **Type:** Hook (documentation function)
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 317–319 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L317-L319)
- **Module/theme:** filter
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_filter_format_disable($format)
```

## Documentation

```text
Perform actions when a text format has been disabled.

@param $format
  The format object of the format being disabled.

@see hook_filter_format_insert()
@see hook_filter_format_update()
```

## Code

```php
function hook_filter_format_disable($format) {
  mymodule_cache_rebuild();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_filter_format_disable()".

- [filter_test_filter_format_disable()](../../simpletest/tests/filter_test.module/filter_test_filter_format_disable.md) — `modules/simpletest/tests/filter_test.module`
- [text_filter_format_disable()](../../field/modules/text/text.module/text_filter_format_disable.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
