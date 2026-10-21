# DrupalHTMLIdentifierTestCase::testDrupalCleanCSSIdentifier()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1021–1046 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1021-L1046)
- **Class:** [DrupalHTMLIdentifierTestCase](../DrupalHTMLIdentifierTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalCleanCSSIdentifier()
```

## Documentation

```text
Tests that drupal_clean_css_identifier() cleans the identifier properly.
```

## Code

```php
  function testDrupalCleanCSSIdentifier() {
    // Verify that no valid ASCII characters are stripped from the identifier.
    $identifier = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ-0123456789';
    $this->assertIdentical(drupal_clean_css_identifier($identifier, array()), $identifier, 'Verify valid ASCII characters pass through.');

    // Verify that valid UTF-8 characters are not stripped from the identifier.
    $identifier = '¡¢£¤¥';
    $this->assertIdentical(drupal_clean_css_identifier($identifier, array()), $identifier, 'Verify valid UTF-8 characters pass through.');

    // Verify that invalid characters (including non-breaking space) are stripped from the identifier.
    $this->assertIdentical(drupal_clean_css_identifier('invalid !"#$%&\'()*+,./:;<=>?@[\\]^`{|}~ identifier', array()), 'invalididentifier', 'Strip invalid characters.');

    // Verify that double underscores are replaced in the identifier by default.
    $identifier = 'css__identifier__with__double__underscores';
    $expected = 'css--identifier--with--double--underscores';
    $this->assertIdentical(drupal_clean_css_identifier($identifier), $expected, 'Verify double underscores are replaced with double hyphens by default.');

    // Verify that double underscores are preserved in the identifier if the
    // variable allow_css_double_underscores is set to TRUE.
    $this->setAllowCSSDoubleUnderscores(TRUE);
    $this->assertIdentical(drupal_clean_css_identifier($identifier), $identifier, 'Verify double underscores are preserved if the allow_css_double_underscores set to TRUE.');

    // To avoid affecting other test cases, set the variable
    // allow_css_double_underscores to FALSE which is the default value.
    $this->setAllowCSSDoubleUnderscores(FALSE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
