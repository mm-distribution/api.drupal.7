# ProfileTestCase::createProfileField()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 37–72 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L37-L72)
- **Class:** [ProfileTestCase](../ProfileTestCase.md)
- **Module/theme:** profile

## Signature

```php
function createProfileField($type = 'textfield', $category = 'simpletest', $edit = array())
```

## Documentation

```text
Create a profile field.

@param $type
  The field type to be created.
@param $category
  The category in which the field should be created.
@param $edit
  Additional parameters to be submitted.
@return
  The fid of the field that was just created.
```

## Code

```php
  function createProfileField($type = 'textfield', $category = 'simpletest', $edit = array()) {
    $edit['title'] = $title = $this->randomName(8);
    $edit['name'] = $form_name = 'profile_' . $title;
    $edit['category'] = $category;
    $edit['explanation'] = $this->randomName(50);

    $this->drupalPost('admin/config/people/profile/add/' . $type, $edit, t('Save field'));
    $fid = db_query("SELECT fid FROM {profile_field} WHERE title = :title", array(':title' => $title))->fetchField();
    $this->assertTrue($fid, 'New Profile field has been entered in the database');

    // Check that the new field is appearing on the user edit form.
    $this->drupalGet('user/' . $this->admin_user->uid . '/edit/' . $category);

    // Checking field.
    if ($type == 'date') {
      $this->assertField($form_name . '[month]', 'Found month selection field');
      $this->assertField($form_name . '[day]', 'Found day selection field');
      $this->assertField($form_name . '[year]', 'Found day selection field');
    }
    else {
      $this->assertField($form_name , format_string('Found form named @name', array('@name' => $form_name)));
    }

    // Checking name.
    $this->assertText($title, format_string('Checking title for field %title', array('%title' => $title)));
    // Checking explanation.
    $this->assertText($edit['explanation'], format_string('Checking explanation for field %title', array('%title' => $title)));

    return array(
      'fid' => $fid,
      'type' => $type,
      'form_name' => $form_name,
      'title' => $title,
      'category' => $category,
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
