# CascadingStylesheetsTestCase::testRenderOverride()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 955–974 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L955-L974)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderOverride()
```

## Documentation

```text
Test CSS override.
```

## Code

```php
  function testRenderOverride() {
    $system = drupal_get_path('module', 'system');
    $simpletest = drupal_get_path('module', 'simpletest');

    drupal_add_css($system . '/system.base.css');
    drupal_add_css($simpletest . '/tests/system.base.css');

    // The dummy stylesheet should be the only one included.
    $styles = drupal_get_css();
    $this->assert(strpos($styles, $simpletest . '/tests/system.base.css') !== FALSE, 'The overriding CSS file is output.');
    $this->assert(strpos($styles, $system . '/system.base.css') === FALSE, 'The overridden CSS file is not output.');

    drupal_add_css($simpletest . '/tests/system.base.css');
    drupal_add_css($system . '/system.base.css');

    // The standard stylesheet should be the only one included.
    $styles = drupal_get_css();
    $this->assert(strpos($styles, $system . '/system.base.css') !== FALSE, 'The overriding CSS file is output.');
    $this->assert(strpos($styles, $simpletest . '/tests/system.base.css') === FALSE, 'The overridden CSS file is not output.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
