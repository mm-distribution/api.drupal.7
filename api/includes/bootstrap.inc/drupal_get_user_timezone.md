# drupal_get_user_timezone()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2634–2644 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2634-L2644)

## Signature

```php
function drupal_get_user_timezone()
```

## Documentation

```text
Returns the time zone of the current user.
```

## Code

```php
function drupal_get_user_timezone() {
  global $user;
  if (variable_get('configurable_timezones', 1) && $user->uid && $user->timezone) {
    return $user->timezone;
  }
  else {
    // Ignore PHP strict notice if time zone has not yet been set in the php.ini
    // configuration.
    return variable_get('date_default_timezone', @date_default_timezone_get());
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
