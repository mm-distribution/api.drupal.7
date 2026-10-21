# ProfileTestCase::deleteProfileField()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 160–164 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L160-L164)
- **Class:** [ProfileTestCase](../ProfileTestCase.md)
- **Module/theme:** profile

## Signature

```php
function deleteProfileField($field)
```

## Documentation

```text
Delete a profile field.

@param $field
  The field to be deleted.
```

## Code

```php
  function deleteProfileField($field) {
    $this->drupalPost('admin/config/people/profile/delete/' . $field['fid'], array(), t('Delete'));
    $this->drupalGet('admin/config/people/profile');
    $this->assertNoText($field['title'], format_string('Checking deleted field %title', array('%title' => $field['title'])));
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
