# ProfileTestFields::testProfileFields()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 180–208 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L180-L208)
- **Class:** [ProfileTestFields](../ProfileTestFields.md)
- **Module/theme:** profile

## Signature

```php
function testProfileFields()
```

## Documentation

```text
Test each of the field types. List selection and date fields are tested
separately because they need some special handling.
```

## Code

```php
  function testProfileFields() {
    $this->drupalLogin($this->admin_user);

    // Set test values for every field type.
    $field_types = array(
      'textfield' => $this->randomName(),
      'textarea' => $this->randomName(),
      'list' => $this->randomName(),
      'checkbox' => 1,
      // An underscore is an invalid character in a domain name. The method randomName can
      // return an underscore.
      'url' => 'http://www.' . str_replace('_', '', $this->randomName(10)) . '.org',
    );

    // For each field type, create a field, give it a value, update the field,
    // and delete the field.
    foreach ($field_types as $type => $value) {
      $field = $this->createProfileField($type);
      $this->setProfileField($field, $value);
      $edit = array(
        'name' => $field['form_name'],
        'title' => $this->randomName(),
        'category' => $field['category'],
        'explanation' => $this->randomName(),
      );
      $field = $this->updateProfileField($field['fid'], $field['type'], $edit);
      $this->deleteProfileField($field);
    }
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
