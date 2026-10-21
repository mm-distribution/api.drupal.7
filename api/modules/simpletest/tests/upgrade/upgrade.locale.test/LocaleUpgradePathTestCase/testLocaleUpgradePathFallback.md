# LocaleUpgradePathTestCase::testLocaleUpgradePathFallback()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.locale.test`](../_file.md), lines 74–98 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test#L74-L98)
- **Class:** [LocaleUpgradePathTestCase](../LocaleUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testLocaleUpgradePathFallback()
```

## Documentation

```text
Test an upgrade with path-based (with fallback) negotiation.
```

## Code

```php
  public function testLocaleUpgradePathFallback() {
    if ($this->skipUpgradeTest) {
      return;
    }
    // LANGUAGE_NEGOTIATION_PATH.
    $this->variable_set('language_negotiation', 2);

    // Set the language of the admin user to English.
    db_update('users')
      ->fields(array('language' => 'en'))
      ->condition('uid', 1)
      ->execute();

    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // Both prefixes should be active.
    $this->assertPageInLanguage('fr', 'fr');
    $this->assertPageInLanguage('en', 'en');

    // The home page should be in the admin user language.
    $this->assertPageInLanguage('', 'en');

    // The language switcher block should be displayed.
    $this->assertRaw('block-locale-language', 'The language switcher block is displayed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.locale.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
