# PathLanguageUITestCase::setUp()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 492–508 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L492-L508)
- **Class:** [PathLanguageUITestCase](../PathLanguageUITestCase.md)
- **Module/theme:** path

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('path', 'locale');

    // Create and login user.
    $web_user = $this->drupalCreateUser(array('edit any page content', 'create page content', 'administer url aliases', 'create url aliases', 'administer languages', 'access administration pages'));
    $this->drupalLogin($web_user);

    // Enable French language.
    $edit = array();
    $edit['langcode'] = 'fr';

    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Enable URL language detection and selection.
    $edit = array('language[enabled][locale-url]' => 1);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
