# TextTranslationTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 442–466 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L442-L466)
- **Class:** [TextTranslationTestCase](../TextTranslationTestCase.md)
- **Module/theme:** text

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('locale', 'translation');

    $full_html_format = filter_format_load('full_html');
    $this->format = $full_html_format->format;
    $this->admin = $this->drupalCreateUser(array(
      'administer languages',
      'administer content types',
      'access administration pages',
      'bypass node access',
      'administer fields',
      filter_permission_name($full_html_format),
    ));
    $this->translator = $this->drupalCreateUser(array('create article content', 'edit own article content', 'translate content'));

    // Enable an additional language.
    $this->drupalLogin($this->admin);
    $edit = array('langcode' => 'fr');
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Set "Article" content type to use multilingual support with translation.
    $edit = array('language_content_type' => 2);
    $this->drupalPost('admin/structure/types/manage/article', $edit, t('Save content type'));
    $this->assertRaw(t('The content type %type has been updated.', array('%type' => 'Article')), 'Article content type has been updated.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
