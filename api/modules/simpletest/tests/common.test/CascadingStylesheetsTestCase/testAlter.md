# CascadingStylesheetsTestCase::testAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 979–992 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L979-L992)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlter()
```

## Documentation

```text
Tests Locale module's CSS Alter to include RTL overrides.
```

## Code

```php
  function testAlter() {
    // Switch the language to a right to left language and add system.base.css.
    global $language;
    $language->direction = LANGUAGE_RTL;
    $path = drupal_get_path('module', 'system');
    drupal_add_css($path . '/system.base.css');

    // Check to see if system.base-rtl.css was also added.
    $styles = drupal_get_css();
    $this->assert(strpos($styles, $path . '/system.base-rtl.css') !== FALSE, 'CSS is alterable as right to left overrides are added.');

    // Change the language back to left to right.
    $language->direction = LANGUAGE_LTR;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
