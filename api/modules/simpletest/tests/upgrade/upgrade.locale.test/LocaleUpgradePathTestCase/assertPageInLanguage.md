# LocaleUpgradePathTestCase::assertPageInLanguage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.locale.test`](../_file.md), lines 139–154 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test#L139-L154)
- **Class:** [LocaleUpgradePathTestCase](../LocaleUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function assertPageInLanguage($path, $langcode)
```

## Documentation

```text
Asserts that a page exists and is in the specified language.
```

## Code

```php
  public function assertPageInLanguage($path, $langcode) {
    if (isset($path)) {
      $this->drupalGet($path);
    }

    if (!$this->assertResponse(200)) {
      return FALSE;
    }

    if ($this->parse()) {
      return $this->assertIdentical($langcode, (string) $this->elements['xml:lang']);
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.locale.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
