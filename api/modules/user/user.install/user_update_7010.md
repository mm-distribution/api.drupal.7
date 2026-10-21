# user_update_7010()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 662–706 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L662-L706)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7010()
```

## Documentation

```text
Update the {user}.signature_format column.
```

## Code

```php
function user_update_7010() {
  // Update the database column to allow NULL values.
  db_change_field('users', 'signature_format', 'signature_format', array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => FALSE,
    'description' => 'The {filter_format}.format of the signature.',
  ));

  // Replace the signature format with NULL if the signature is empty and does
  // not already have a stored text format.
  //
  // In Drupal 6, "0" (the former FILTER_FORMAT_DEFAULT constant) could be used
  // to indicate this situation, but in Drupal 7, only NULL is supported. This
  // update therefore preserves the ability of user accounts which were never
  // given a signature (for example, if the site did not have user signatures
  // enabled, or if the user never edited their account information) to not
  // have a particular text format assumed for them the first time the
  // signature is edited.
  db_update('users')
    ->fields(array('signature_format' => NULL))
    ->condition('signature', '')
    ->condition('signature_format', 0)
    ->execute();

  // There are a number of situations in which a Drupal 6 site could store
  // content with a nonexistent text format. This includes text formats that
  // had later been deleted, or non-empty content stored with a value of "0"
  // (the former FILTER_FORMAT_DEFAULT constant). Drupal 6 would filter this
  // content using whatever the site-wide default text format was at the moment
  // the text was being displayed.
  //
  // In Drupal 7, this behavior is no longer supported, and all content must be
  // stored with an explicit text format (or it will not be displayed when it
  // is filtered). Therefore, to preserve the behavior of the site after the
  // upgrade, we must replace all instances described above with the current
  // value of the (old) site-wide default format at the moment of the upgrade.
  $existing_formats = db_query("SELECT format FROM {filter_format}")->fetchCol();
  $default_format = variable_get('filter_default_format', 1);
  db_update('users')
    ->fields(array('signature_format' => $default_format))
    ->isNotNull('signature_format')
    ->condition('signature_format', $existing_formats, 'NOT IN')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
