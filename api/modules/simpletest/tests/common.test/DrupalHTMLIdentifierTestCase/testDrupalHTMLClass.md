# DrupalHTMLIdentifierTestCase::testDrupalHTMLClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1062–1065 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1062-L1065)
- **Class:** [DrupalHTMLIdentifierTestCase](../DrupalHTMLIdentifierTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHTMLClass()
```

## Documentation

```text
Tests that drupal_html_class() cleans the class name properly.
```

## Code

```php
  function testDrupalHTMLClass() {
    // Verify Drupal coding standards are enforced.
    $this->assertIdentical(drupal_html_class('CLASS NAME_[Ü]'), 'class-name--ü', 'Enforce Drupal coding standards.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
