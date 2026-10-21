# DrupalGotoTest::testDrupalGotoAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1494–1499 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1494-L1499)
- **Class:** [DrupalGotoTest](../DrupalGotoTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalGotoAlter()
```

## Documentation

```text
Test hook_drupal_goto_alter().
```

## Code

```php
  function testDrupalGotoAlter() {
    $this->drupalGet('common-test/drupal_goto/redirect_fail');

    $this->assertNoText(t("Drupal goto failed to stop program"), "Drupal goto stopped program.");
    $this->assertNoText('drupal_goto_fail', "Drupal goto redirect failed.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
