# filter_update_7005()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 352–442 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L352-L442)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7005()
```

## Documentation

```text
Integrate text formats with the user permissions system.

This function converts text format role assignments to use the new text
format permissions introduced in Drupal 7, creates a fallback (plain text)
format that is available to all users, and explicitly sets the text format
in cases that used to rely on a single site-wide default.
```

## Code

```php
function filter_update_7005() {
  // Move role data from the filter system to the user permission system.
  $all_roles = array_keys(user_roles());
  $default_format = variable_get('filter_default_format', 1);
  $result = db_query("SELECT * FROM {filter_format}");
  foreach ($result as $format) {
    // We need to assign the default format to all roles (regardless of what
    // was stored in the database) to preserve the behavior of the site at the
    // moment of the upgrade.
    $format_roles = ($format->format == $default_format ? $all_roles : explode(',', $format->roles));
    foreach ($format_roles as $format_role) {
      if (in_array($format_role, $all_roles)) {
        _update_7000_user_role_grant_permissions($format_role, array('use text format ' . $format->format), 'filter');
      }
    }
  }

  // Drop the roles field from the {filter_format} table.
  db_drop_field('filter_format', 'roles');

  // Add a fallback text format which outputs plain text and appears last on
  // the list for all users. Generate a unique name for it, starting with
  // "Plain text".
  $start_name = 'Plain text';
  $format_name = $start_name;
  while ($format = db_query('SELECT format FROM {filter_format} WHERE name = :name', array(':name' => $format_name))->fetchField()) {
    $id = empty($id) ? 2 : $id + 1;
    $format_name = $start_name . ' ' . $id;
  }

  // Insert the filter format.
  $format_id = db_insert('filter_format')
    ->fields(array(
      'name' => $format_name,
      'cache' => 1,
      'weight' => 1,
      'status' => 1,
    ))
    ->execute();

  // This format should output plain text, so we escape all HTML and apply the
  // line break and URL filters only.
  db_insert('filter')
    ->fields(array(
      'format',
      'name',
      'weight',
      'status',
      'module',
      'settings',
    ))
    ->values(array(
      'format' => $format_id,
      'name' => 'filter_html_escape',
      'weight' => 0,
      'status' => 1,
      'module' => 'filter',
      'settings' => serialize(array()),
    ))
    ->values(array(
      'format' => $format_id,
      'name' => 'filter_url',
      'weight' => 1,
      'status' => 1,
      'module' => 'filter',
      'settings' => serialize(array()),
    ))
    ->values(array(
      'format' => $format_id,
      'name' => 'filter_autop',
      'weight' => 2,
      'status' => 1,
      'module' => 'filter',
      'settings' => serialize(array()),
    ))
    ->execute();

  variable_set('filter_fallback_format', $format_id);
  drupal_set_message('A new <em>Plain text</em> format has been created which will be available to all users. You can configure this text format on the <a href="' . url('admin/config/content/formats/' . $format) . '">text format configuration page</a>.');

  // Move the former site-wide default text format to the top of the list, so
  // that it continues to be the default text format for all users.
  db_update('filter_format')
    ->fields(array('weight' => -1))
    ->condition('format', $default_format)
    ->execute();

  // We do not delete the 'filter_default_format' variable, since other modules
  // need it in their update functions; for an example, see user_update_7010().
  // @todo This variable can be deleted in Drupal 8.
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
