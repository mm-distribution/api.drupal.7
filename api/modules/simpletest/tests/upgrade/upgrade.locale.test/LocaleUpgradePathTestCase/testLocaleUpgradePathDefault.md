# LocaleUpgradePathTestCase::testLocaleUpgradePathDefault()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.locale.test`](../_file.md), lines 48–69 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test#L48-L69)
- **Class:** [LocaleUpgradePathTestCase](../LocaleUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testLocaleUpgradePathDefault()
```

## Documentation

```text
Test an upgrade with path-based negotiation.
```

## Code

```php
  public function testLocaleUpgradePathDefault() {
    if ($this->skipUpgradeTest) {
      return;
    }
    // LANGUAGE_NEGOTIATION_PATH_DEFAULT.
    $this->variable_set('language_negotiation', 1);

    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // The home page should be in French.
    $this->assertPageInLanguage('', 'fr');

    // The language switcher block should be displayed.
    $this->assertRaw('block-locale-language', 'The language switcher block is displayed.');

    // The French prefix should not be active because French is the default language.
    $this->drupalGet('fr');
    $this->assertResponse(404);

    // The English prefix should be active.
    $this->assertPageInLanguage('en', 'en');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.locale.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
