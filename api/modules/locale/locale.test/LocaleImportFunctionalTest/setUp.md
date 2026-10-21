# LocaleImportFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 929–934 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L929-L934)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
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

    $this->admin_user = $this->drupalCreateUser(array('administer languages', 'translate interface', 'access administration pages'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
