# ProfileTestDate::testProfileDateField()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 256–285 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L256-L285)
- **Class:** [ProfileTestDate](../ProfileTestDate.md)
- **Module/theme:** profile

## Signature

```php
function testProfileDateField()
```

## Documentation

```text
Create a date field, give it a value, update and delete the field.
```

## Code

```php
  function testProfileDateField() {
    $this->drupalLogin($this->admin_user);

    variable_set('date_format_short', 'm/d/Y - H:i');
    $field = $this->createProfileField('date');

    // Set date to January 09, 1983
    $edit = array(
      $field['form_name'] . '[month]' => 1,
      $field['form_name'] . '[day]' => 9,
      $field['form_name'] . '[year]' => 1983,
    );

    $this->drupalPost('user/' . $this->normal_user->uid . '/edit/' . $field['category'], $edit, t('Save'));

    // Check profile page.
    $this->drupalGet('user/' . $this->normal_user->uid);
    $this->assertText($field['title'], format_string('Found profile field with title %title', array('%title' => $field['title'])));

    $this->assertText('01/09/1983', 'Found date profile field.');

    $edit = array(
      'name' => $field['form_name'],
      'title' => $this->randomName(),
      'category' => $field['category'],
      'explanation' => $this->randomName(),
    );
    $field = $this->updateProfileField($field['fid'], $field['type'], $edit);
    $this->deleteProfileField($field);
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
