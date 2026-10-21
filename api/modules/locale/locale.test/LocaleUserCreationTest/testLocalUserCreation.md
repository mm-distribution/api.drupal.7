# LocaleUserCreationTest::testLocalUserCreation()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1926–2004 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1926-L2004)
- **Class:** [LocaleUserCreationTest](../LocaleUserCreationTest.md)
- **Module/theme:** locale

## Signature

```php
function testLocalUserCreation()
```

## Documentation

```text
Functional test for language handling during user creation.
```

## Code

```php
  function testLocalUserCreation() {
    // User to add and remove language and create new users.
    $admin_user = $this->drupalCreateUser(array('administer languages', 'access administration pages', 'administer users'));
    $this->drupalLogin($admin_user);

    // Add predefined language.
    $langcode = 'fr';
    $edit = array(
      'langcode' => 'fr',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));
    $this->assertText($langcode, 'Language added successfully.');
    $this->assertEqual($this->getUrl(), url('admin/config/regional/language', array('absolute' => TRUE)), 'Correct page redirection.');

    // Set language negotiation.
    $edit = array(
      'language[enabled][locale-url]' => TRUE,
    );
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));
    $this->assertText(t('Language negotiation configuration saved.'), 'Set language negotiation.');

    // Check if the language selector is available on admin/people/create and
    // set to the currently active language.
    $this->drupalGet($langcode . '/admin/people/create');
    $this->assertFieldChecked("edit-language-$langcode", 'Global language set in the language selector.');

    // Create a user with the admin/people/create form and check if the correct
    // language is set.
    $username = $this->randomName(10);
    $edit = array(
      'name' => $username,
      'mail' => $this->randomName(4) . '@example.com',
      'pass[pass1]' => $username,
      'pass[pass2]' => $username,
    );

    $this->drupalPost($langcode . '/admin/people/create', $edit, t('Create new account'));

    $user = user_load_by_name($username);
    $this->assertEqual($user->language, $langcode, 'New user has correct language set.');

    // Register a new user and check if the language selector is hidden.
    $this->drupalLogout();

    $this->drupalGet($langcode . '/user/register');
    $this->assertNoFieldByName('language[fr]', 'Language selector is not accessible.');

    $username = $this->randomName(10);
    $edit = array(
      'name' => $username,
      'mail' => $this->randomName(4) . '@example.com',
    );

    $this->drupalPost($langcode . '/user/register', $edit, t('Create new account'));

    $user = user_load_by_name($username);
    $this->assertEqual($user->language, $langcode, 'New user has correct language set.');

    // Test if the admin can use the language selector and if the
    // correct language is was saved.
    $user_edit = $langcode . '/user/' . $user->uid . '/edit';

    $this->drupalLogin($admin_user);
    $this->drupalGet($user_edit);
    $this->assertFieldChecked("edit-language-$langcode", 'Language selector is accessible and correct language is selected.');

    // Set pass_raw so we can login the new user.
    $user->pass_raw = $this->randomName(10);
    $edit = array(
      'pass[pass1]' => $user->pass_raw,
      'pass[pass2]' => $user->pass_raw,
    );

    $this->drupalPost($user_edit, $edit, t('Save'));

    $this->drupalLogin($user);
    $this->drupalGet($user_edit);
    $this->assertFieldChecked("edit-language-$langcode", 'Language selector is accessible and correct language is selected.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
