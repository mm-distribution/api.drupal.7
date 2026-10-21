# LocaleLanguageSwitchingFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1617–1623 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1617-L1623)
- **Class:** [LocaleLanguageSwitchingFunctionalTest](../LocaleLanguageSwitchingFunctionalTest.md)
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
    parent::setUp('locale');

    // Create and login user.
    $admin_user = $this->drupalCreateUser(array('administer blocks', 'administer languages', 'translate interface', 'access administration pages'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
