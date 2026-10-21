# FormatDateUnitTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2932–2943 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2932-L2943)
- **Class:** [FormatDateUnitTest](../FormatDateUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('locale');
    variable_set('configurable_timezones', 1);
    variable_set('date_format_long', 'l, j. F Y - G:i');
    variable_set('date_format_medium', 'j. F Y - G:i');
    variable_set('date_format_short', 'Y M j - g:ia');
    variable_set('locale_custom_strings_' . self::LANGCODE, array(
      '' => array('Sunday' => 'domingo'),
      'Long month name' => array('March' => 'marzo'),
    ));
    $this->refreshVariables();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
