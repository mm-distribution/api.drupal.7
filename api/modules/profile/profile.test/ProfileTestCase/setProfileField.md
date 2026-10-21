# ProfileTestCase::setProfileField()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 131–152 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L131-L152)
- **Class:** [ProfileTestCase](../ProfileTestCase.md)
- **Module/theme:** profile

## Signature

```php
function setProfileField($field, $value = NULL)
```

## Documentation

```text
Set the profile field to a random value

@param $field
  The field that should be set.
@param $value
  The value for the field, defaults to a random string.
@return
  The value that has been assigned to
```

## Code

```php
  function setProfileField($field, $value = NULL) {

    if (!isset($value)) {
      $value = $this->randomName();
    }

    $edit = array(
      $field['form_name'] => $value,
    );
    $this->drupalPost('user/' . $this->normal_user->uid . '/edit/' . $field['category'], $edit, t('Save'));

    // Check profile page.
    $content = $this->drupalGet('user/' . $this->normal_user->uid);
    $this->assertText($field['title'], format_string('Found profile field with title %title', array('%title' => $field['title'])));

    if ($field['type'] != 'checkbox') {
      // $value must be cast to a string in order to be found by assertText.
      $this->assertText("$value", format_string('Found profile field with value %value', array('%value' => $value)));
    }

    return $value;
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
