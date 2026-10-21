# common_test_drupal_render_printing_pre_render()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 124–127 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L124-L127)
- **Module/theme:** batch_test

## Signature

```php
function common_test_drupal_render_printing_pre_render($elements)
```

## Documentation

```text
Applies #printed to an element to help test #pre_render.
```

## Code

```php
function common_test_drupal_render_printing_pre_render($elements) {
  $elements['#printed'] = TRUE;
  return $elements;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
