# LocaleUpgradePathTestCase::testLocaleUpgradeDomain()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.locale.test`](../_file.md), lines 103–134 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test#L103-L134)
- **Class:** [LocaleUpgradePathTestCase](../LocaleUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testLocaleUpgradeDomain()
```

## Documentation

```text
Test an upgrade with domain-based negotiation.
```

## Code

```php
  public function testLocaleUpgradeDomain() {
    if ($this->skipUpgradeTest) {
      return;
    }
    // LANGUAGE_NEGOTIATION_DOMAIN.
    $this->variable_set('language_negotiation', 3);

    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // The home page should be in French.
    $this->assertPageInLanguage('', 'fr');

    // The language switcher block should be displayed.
    $this->assertRaw('block-locale-language', 'The language switcher block is displayed.');

    // The language switcher block should point to http://en.example.com.
    $language_links = $this->xpath('//ul[contains(@class, :class)]/li/a', array(':class' => 'language-switcher-locale-url'));
    $found_english_link = FALSE;
    foreach ($language_links as $link) {
      if ((string) $link['href'] == 'http://en.example.com/') {
        $found_english_link = TRUE;
      }
    }
    $this->assertTrue($found_english_link, 'The English link points to the correct domain.');

    // Both prefixes should be inactive.
    $this->drupalGet('en');
    $this->assertResponse(404);
    $this->drupalGet('fr');
    $this->assertResponse(404);

  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.locale.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
