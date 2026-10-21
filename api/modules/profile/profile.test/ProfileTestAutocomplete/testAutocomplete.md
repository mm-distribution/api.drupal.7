# ProfileTestAutocomplete::testAutocomplete()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 330–378 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L330-L378)
- **Class:** [ProfileTestAutocomplete](../ProfileTestAutocomplete.md)
- **Module/theme:** profile

## Signature

```php
function testAutocomplete()
```

## Documentation

```text
Tests profile field autocompletion and access.
```

## Code

```php
  function testAutocomplete() {
    $this->drupalLogin($this->admin_user);

    // Create a new profile field with autocompletion enabled.
    $category = $this->randomName();
    $field = $this->createProfileField('textfield', $category, array('weight' => 1, 'autocomplete' => 1));

    // Enter profile field value.
    $field['value'] = $this->randomName();
    $this->setProfileField($field, $field['value']);

    // Set some html for what we want to see in the page output later.
    // Autocomplete always uses non-clean URLs.
    $current_clean_url = isset($GLOBALS['conf']['clean_url']) ? $GLOBALS['conf']['clean_url'] : NULL;
    $GLOBALS['conf']['clean_url'] = 0;
    $autocomplete_url = url('profile/autocomplete/' . $field['fid'], array('absolute' => TRUE, 'script' => 'index.php'));
    $GLOBALS['conf']['clean_url'] = $current_clean_url;
    $autocomplete_id = drupal_html_id('edit-' . $field['form_name'] . '-autocomplete');
    $autocomplete_html = '<input type="hidden" id="' . $autocomplete_id . '" value="' . $autocomplete_url . '" disabled="disabled" class="autocomplete" />';

    // Check that autocompletion html is found on the user's profile edit page.
    $this->drupalGet('user/' . $this->admin_user->uid . '/edit/' . $category);
    $this->assertRaw($autocomplete_html, 'Autocomplete found.');
    $this->assertFieldByXPath(
      '//input[@type="text" and @name="' . $field['form_name'] . '" and contains(@class, "form-autocomplete")]',
      '',
      'Text input field found'
    );
    $this->assertRaw('misc/autocomplete.js', 'Autocomplete JavaScript found.');
    $this->assertRaw('class="form-text form-autocomplete"', 'Autocomplete form element class found.');

    // Check the autocompletion path using the first letter of our user's profile
    // field value to make sure access is allowed and a valid result if found.
    $this->drupalGet('profile/autocomplete/' . $field['fid'] . '/' . $field['value'][0]);
    $this->assertResponse(200, 'Autocomplete path allowed to user with permission.');
    $this->assertRaw($field['value'], 'Autocomplete value found.');

    // Logout and login with a user without the 'access user profiles' permission.
    $this->drupalLogout();
    $this->drupalLogin($this->normal_user);

    // Check that autocompletion html is not found on the user's profile edit page.
    $this->drupalGet('user/' . $this->normal_user->uid . '/edit/' . $category);
    $this->assertNoRaw($autocomplete_html, 'Autocomplete not found.');

    // User should be denied access to the profile autocomplete path.
    $this->drupalGet('profile/autocomplete/' . $field['fid'] . '/' . $field['value'][0]);
    $this->assertResponse(403, 'Autocomplete path denied to user without permission.');
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
