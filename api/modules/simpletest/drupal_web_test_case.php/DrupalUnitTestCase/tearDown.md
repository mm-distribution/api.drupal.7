# DrupalUnitTestCase::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 825–843 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L825-L843)
- **Class:** [DrupalUnitTestCase](../DrupalUnitTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function tearDown()
```

## Documentation

_No docblock in source._

## Code

```php
  protected function tearDown() {
    global $conf, $language;

    // Get back to the original connection.
    Database::removeConnection('default');
    Database::renameConnection('simpletest_original_default', 'default');

    $conf['file_public_path'] = $this->originalFileDirectory;
    // Restore modules if necessary.
    if (isset($this->originalModuleList)) {
      module_list(TRUE, FALSE, FALSE, $this->originalModuleList);
    }

    // Reset language.
    $language = $this->originalLanguage;
    if ($this->originalLanguageDefault) {
      $GLOBALS['conf']['language_default'] = $this->originalLanguageDefault;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
