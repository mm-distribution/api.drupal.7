# DrupalHTMLIdentifierTestCase::setAllowCSSDoubleUnderscores()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1054–1057 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1054-L1057)
- **Class:** [DrupalHTMLIdentifierTestCase](../DrupalHTMLIdentifierTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setAllowCSSDoubleUnderscores($value)
```

## Documentation

```text
Set the variable allow_css_double_underscores and reset the cache.

@param $value bool
  A new value to be set to allow_css_double_underscores.
```

## Code

```php
  function setAllowCSSDoubleUnderscores($value) {
    $GLOBALS['conf']['allow_css_double_underscores'] = $value;
    drupal_static_reset('drupal_clean_css_identifier:allow_css_double_underscores');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
