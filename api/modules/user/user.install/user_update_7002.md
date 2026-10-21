# user_update_7002()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 488–556 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L488-L556)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7002(&$sandbox)
```

## Documentation

```text
Convert user time zones from time zone offsets to time zone names.
```

## Code

```php
function user_update_7002(&$sandbox) {
  $sandbox['#finished'] = 0;

  // Multi-part update.
  if (!isset($sandbox['user_from'])) {
    db_change_field('users', 'timezone', 'timezone', array('type' => 'varchar', 'length' => 32, 'not null' => FALSE));
    $sandbox['user_from'] = 0;
    $sandbox['user_count'] = db_query("SELECT COUNT(uid) FROM {users}")->fetchField();
    $sandbox['user_not_migrated'] = 0;
  }
  else {
    $timezones = system_time_zones();
    // Update this many per page load.
    $count = 10000;
    $contributed_date_module = db_field_exists('users', 'timezone_name');
    $contributed_event_module = db_field_exists('users', 'timezone_id');

    $results = db_query_range("SELECT uid FROM {users} ORDER BY uid", $sandbox['user_from'], $count);
    foreach ($results as $account) {
      $timezone = NULL;
      // If the contributed Date module has created a users.timezone_name
      // column, use this data to set each user's time zone.
      if ($contributed_date_module) {
        $date_timezone = db_query("SELECT timezone_name FROM {users} WHERE uid = :uid", array(':uid' => $account->uid))->fetchField();
        if (isset($timezones[$date_timezone])) {
          $timezone = $date_timezone;
        }
      }
      // If the contributed Event module has stored user time zone information
      // use that information to update the user accounts.
      if (!$timezone && $contributed_event_module) {
        try {
          $event_timezone = db_query("SELECT t.name FROM {users} u LEFT JOIN {event_timezones} t ON u.timezone_id = t.timezone WHERE u.uid = :uid", array(':uid' => $account->uid))->fetchField();
          $event_timezone = str_replace(' ', '_', $event_timezone);
          if (isset($timezones[$event_timezone])) {
            $timezone = $event_timezone;
          }
        }
        catch (PDOException $e) {
          // Ignore error if event_timezones table does not exist or unexpected
          // schema found.
        }
      }
      if ($timezone) {
        db_update('users')
          ->fields(array('timezone' => $timezone))
          ->condition('uid', $account->uid)
          ->execute();
      }
      else {
        $sandbox['user_not_migrated']++;
        db_update('users')
          ->fields(array('timezone' => NULL))
          ->condition('uid', $account->uid)
          ->execute();
      }
      $sandbox['user_from']++;
    }

    $sandbox['#finished'] = $sandbox['user_from'] / $sandbox['user_count'];
    if ($sandbox['user_from'] == $sandbox['user_count']) {
      if ($sandbox['user_not_migrated'] > 0) {
        variable_set('empty_timezone_message', 1);
        drupal_set_message(format_string('Some user time zones have been emptied and need to be set to the correct values. Use the new <a href="@config-url">time zone options</a> to choose whether to remind users at login to set the correct time zone.', array('@config-url' => url('admin/config/regional/settings'))), 'warning');
      }
      return t('Migrated user time zones');
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
