# ProfileTestSelect::testProfileSelectionField()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 223–241 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L223-L241)
- **Class:** [ProfileTestSelect](../ProfileTestSelect.md)
- **Module/theme:** profile

## Signature

```php
function testProfileSelectionField()
```

## Documentation

```text
Create a list selection field, give it a value, update and delete the field.
```

## Code

```php
  function testProfileSelectionField() {
    $this->drupalLogin($this->admin_user);

    $edit = array(
      'options' => implode("\n", range(1, 10)),
    );
    $field = $this->createProfileField('selection', 'simpletest', $edit);

    $this->setProfileField($field, rand(1, 10));

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
