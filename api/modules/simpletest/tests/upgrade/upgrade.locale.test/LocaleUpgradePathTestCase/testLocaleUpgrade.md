# LocaleUpgradePathTestCase::testLocaleUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.locale.test`](../_file.md), lines 29–43 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test#L29-L43)
- **Class:** [LocaleUpgradePathTestCase](../LocaleUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testLocaleUpgrade()
```

## Documentation

```text
Test a successful upgrade (no negotiation).
```

## Code

```php
  public function testLocaleUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // The home page should be in French.
    $this->assertPageInLanguage('', 'fr');

    // No prefixed page should exist.
    $this->drupalGet('en');
    $this->assertResponse(404);
    $this->drupalGet('fr');
    $this->assertResponse(404);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.locale.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
