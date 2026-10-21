# profile_view_field()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 278–323 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L278-L323)
- **Module/theme:** profile

## Signature

```php
function profile_view_field($account, $field)
```

## Documentation

_No docblock in source._

## Code

```php
function profile_view_field($account, $field) {
  // Only allow browsing of private fields for admins, if browsing is enabled,
  // and if a user has permission to view profiles. Note that this check is
  // necessary because a user may always see their own profile.
  $browse = user_access('access user profiles')
        && (user_access('administer users') || $field->visibility != PROFILE_PRIVATE)
        && !empty($field->page);

  if (isset($account->{$field->name}) && $value = $account->{$field->name}) {
    switch ($field->type) {
      case 'textarea':
        return check_markup($value, filter_default_format($account), '', TRUE);
      case 'textfield':
      case 'selection':
        return $browse ? l($value, 'profile/' . $field->name . '/' . $value) : check_plain($value);
      case 'checkbox':
        return $browse ? l($field->title, 'profile/' . $field->name) : check_plain($field->title);
      case 'url':
        return '<a href="' . check_url($value) . '">' . check_plain($value) . '</a>';
      case 'date':
        $format = substr(variable_get('date_format_short', 'm/d/Y - H:i'), 0, 5);
        // Note: Avoid PHP's date() because it does not handle dates before
        // 1970 on Windows. This would make the date field useless for e.g.
        // birthdays.
        $replace = array(
          'd' => sprintf('%02d', $value['day']),
          'j' => $value['day'],
          'm' => sprintf('%02d', $value['month']),
          'M' => map_month($value['month']),
          'Y' => $value['year'],
          'H:i' => NULL,
          'g:ia' => NULL,
        );
        return strtr($format, $replace);
      case 'list':
        $values = preg_split("/[,\n\r]/", $value);
        $fields = array();
        foreach ($values as $value) {
          if ($value = trim($value)) {
            $fields[] = $browse ? l($value, 'profile/' . $field->name . '/' . $value) : check_plain($value);
          }
        }
        return implode(', ', $fields);
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
