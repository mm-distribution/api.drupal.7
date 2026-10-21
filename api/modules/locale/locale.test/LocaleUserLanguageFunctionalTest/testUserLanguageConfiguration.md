# LocaleUserLanguageFunctionalTest::testUserLanguageConfiguration()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1829–1902 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1829-L1902)
- **Class:** [LocaleUserLanguageFunctionalTest](../LocaleUserLanguageFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testUserLanguageConfiguration()
```

## Documentation

```text
Test if user can change their default language.
```

## Code

```php
  function testUserLanguageConfiguration() {
    global $base_url;

    // User to add and remove language.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages'));
    // User to change their default language.
    $web_user = $this->drupalCreateUser();

    // Add custom language.
    $this->drupalLogin($admin_user);
    // Code for the language.
    $langcode = 'xx';
    // The English name for the language.
    $name = $this->randomName(16);
    // The native name for the language.
    $native = $this->randomName(16);
    // The domain prefix.
    $prefix = 'xx';
    $edit = array(
      'langcode' => $langcode,
      'name' => $name,
      'native' => $native,
      'prefix' => $prefix,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));

    // Add custom language and disable it.
    // Code for the language.
    $langcode_disabled = 'xx-yy';
    // The English name for the language. This will be translated.
    $name_disabled = $this->randomName(16);
    // The native name for the language.
    $native_disabled = $this->randomName(16);
    // The domain prefix.
    $prefix_disabled = $langcode_disabled;
    $edit = array(
      'langcode' => $langcode_disabled,
      'name' => $name_disabled,
      'native' => $native_disabled,
      'prefix' => $prefix_disabled,
      'direction' => '0',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));
    // Disable the language.
    $edit = array(
      'enabled[' . $langcode_disabled . ']' => FALSE,
    );
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));
    $this->drupalLogout();

    // Login as normal user and edit account settings.
    $this->drupalLogin($web_user);
    $path = 'user/' . $web_user->uid . '/edit';
    $this->drupalGet($path);
    // Ensure language settings fieldset is available.
    $this->assertText(t('Language settings'), 'Language settings available.');
    // Ensure custom language is present.
    $this->assertText($name, 'Language present on form.');
    // Ensure disabled language isn't present.
    $this->assertNoText($name_disabled, 'Disabled language not present on form.');
    // Switch to our custom language.
    $edit = array(
      'language' => $langcode,
    );
    $this->drupalPost($path, $edit, t('Save'));
    // Ensure form was submitted successfully.
    $this->assertText(t('The changes have been saved.'), 'Changes were saved.');
    // Check if language was changed.
    $elements = $this->xpath('//input[@id=:id]', array(':id' => 'edit-language-' . $langcode));
    $this->assertTrue(isset($elements[0]) && !empty($elements[0]['checked']), 'Default language successfully updated.');

    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
