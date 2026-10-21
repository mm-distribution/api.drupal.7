# LocaleCommentLanguageFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2912–2951 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2912-L2951)
- **Class:** [LocaleCommentLanguageFunctionalTest](../LocaleCommentLanguageFunctionalTest.md)
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

    // Create and login user.
    $admin_user = $this->drupalCreateUser(array('administer site configuration', 'administer languages', 'access administration pages', 'administer content types', 'administer comments', 'create article content'));
    $this->drupalLogin($admin_user);

    // Add language.
    $edit = array('langcode' => 'fr');
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Set "Article" content type to use multilingual support.
    $edit = array('language_content_type' => 1);
    $this->drupalPost('admin/structure/types/manage/article', $edit, t('Save content type'));

    // Enable content language negotiation UI.
    variable_set('locale_test_content_language_type', TRUE);

    // Set interface language detection to user and content language detection
    // to URL. Disable inheritance from interface language to ensure content
    // language will fall back to the default language if no URL language can be
    // detected.
    $edit = array(
      'language[enabled][locale-user]' => TRUE,
      'language_content[enabled][locale-url]' => TRUE,
      'language_content[enabled][locale-interface]' => FALSE,
    );
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Change user language preference, this way interface language is always
    // French no matter what path prefix the URLs have.
    $edit = array('language' => 'fr');
    $this->drupalPost("user/{$admin_user->uid}/edit", $edit, t('Save'));

    // Make comment body translatable.
    $field = field_info_field('comment_body');
    $field['translatable'] = TRUE;
    field_update_field($field);
    $this->assertTrue(field_is_translatable('comment', $field), 'Comment body is translatable.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
