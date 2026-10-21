# CascadingStylesheetsTestCase::testDefault()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 766–768 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L766-L768)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDefault()
```

## Documentation

```text
Check default stylesheets as empty.
```

## Code

```php
  function testDefault() {
    $this->assertEqual(array(), drupal_add_css(), 'Default CSS is empty.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
