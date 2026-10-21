# LocaleLanguageNegotiationInfoFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3105–3111 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3105-L3111)
- **Class:** [LocaleLanguageNegotiationInfoFunctionalTest](../LocaleLanguageNegotiationInfoFunctionalTest.md)
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
    require_once DRUPAL_ROOT .'/includes/language.inc';
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages', 'view the administration theme'));
    $this->drupalLogin($admin_user);
    $this->drupalPost('admin/config/regional/language/add', array('langcode' => 'it'), t('Add language'));
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
