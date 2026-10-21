# JavaScriptTestCase::testDoubleSubmitFormProtection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1793–1810 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1793-L1810)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDoubleSubmitFormProtection()
```

## Documentation

```text
Tests the double submit form protection and
'javascript_use_double_submit_protection' variable.
```

## Code

```php
  function testDoubleSubmitFormProtection() {
    // The default front page of the site should have the double submit
    // protection enabled as there is a login block.
    $this->drupalGet('');
    $this->assertRaw('misc/form-single-submit.js', 'Default behavior: Double submit protection is enabled.');

    // The default front page should have the double submit protection disabled
    // when the 'javascript_always_use_jquery' variable is set to FALSE or the
    // 'javascript_use_double_submit_protection' variable is set to FALSE.
    variable_set('javascript_always_use_jquery', FALSE);
    $this->drupalGet('');
    $this->assertNoRaw('misc/form-single-submit.js', 'When "javascript_always_use_jquery" is FALSE: Double submit protection is disabled.');
    variable_del('javascript_always_use_jquery');
    variable_set('javascript_use_double_submit_protection', FALSE);
    $this->drupalGet('');
    $this->assertNoRaw('misc/form-single-submit.js', 'When "javascript_use_double_submit_protection" is FALSE: Double submit protection is disabled.');
    variable_del('javascript_use_double_submit_protection');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
