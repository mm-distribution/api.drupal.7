# LocalePluralFormatTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 794–808 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L794-L808)
- **Class:** [LocalePluralFormatTest](../LocalePluralFormatTest.md)
- **Module/theme:** locale

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('locale', 'locale_test');

    $admin_user = $this->drupalCreateUser(array('administer languages', 'translate interface', 'access administration pages'));
    $this->drupalLogin($admin_user);

    // Import some .po files with formulas to set up the environment.
    // These will also add the languages to the system and enable them.
    $this->importPoFile($this->getPoFileWithSimplePlural(), array(
      'langcode' => 'fr',
    ));
    $this->importPoFile($this->getPoFileWithComplexPlural(), array(
      'langcode' => 'hr',
    ));
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
