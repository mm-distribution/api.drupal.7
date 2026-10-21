# ProfileTestCase::updateProfileField()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 86–119 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L86-L119)
- **Class:** [ProfileTestCase](../ProfileTestCase.md)
- **Module/theme:** profile

## Signature

```php
function updateProfileField($fid, $type = 'textfield', $edit = array())
```

## Documentation

```text
Update a profile field.

@param $fid
  The fid of the field to be updated.
@param $type
  The type of field to be updated.
@param $edit
  Field parameters to be submitted.
@return
  Array representation of the updated field.
```

## Code

```php
  function updateProfileField($fid, $type = 'textfield', $edit = array()) {

    $form_name = $edit['name'];
    $title = $edit['title'];
    $category = $edit['category'];

    $this->drupalPost('admin/config/people/profile/edit/' . $fid, $edit, t('Save field'));

    // Check that the updated field is appearing on the user edit form.
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
