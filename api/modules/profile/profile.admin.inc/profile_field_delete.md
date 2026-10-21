# profile_field_delete()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 396–409 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L396-L409)
- **Module/theme:** profile

## Signature

```php
function profile_field_delete($form, &$form_state, $fid)
```

## Documentation

```text
Menu callback; deletes a field from all user profiles.
```

## Code

```php
function profile_field_delete($form, &$form_state, $fid) {
  $field = db_query("SELECT title FROM {profile_field} WHERE fid = :fid", array(':fid' => $fid))->fetchObject();
  if (!$field) {
    drupal_not_found();
    return;
  }
  $form['fid'] = array('#type' => 'value', '#value' => $fid);
  $form['title'] = array('#type' => 'value', '#value' => $field->title);

  return confirm_form($form,
    t('Are you sure you want to delete the field %field?', array('%field' => $field->title)), 'admin/config/people/profile',
    t('This action cannot be undone. If users have entered values into this field in their profile, these entries will also be deleted. If you want to keep the user-entered data, instead of deleting the field you may wish to <a href="@edit-field">edit this field</a> and change it to a hidden profile field so that it may only be accessed by administrators.', array('@edit-field' => url('admin/config/people/profile/edit/' . $fid))),
    t('Delete'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
