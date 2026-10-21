# LocaleUILanguageNegotiationTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2360–2366 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2360-L2366)
- **Class:** [LocaleUILanguageNegotiationTest](../LocaleUILanguageNegotiationTest.md)
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
    require_once DRUPAL_ROOT . '/includes/language.inc';
    drupal_load('module', 'locale');
    $admin_user = $this->drupalCreateUser(array('administer languages', 'translate interface', 'access administration pages', 'administer blocks'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
