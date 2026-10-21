# _menu_site_is_offline()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3945–3966 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3945-L3966)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_site_is_offline($check_only = FALSE)
```

## Documentation

```text
Checks whether the site is in maintenance mode.

This function will log the current user out and redirect to front page
if the current user has no 'access site in maintenance mode' permission.

@param $check_only
  If this is set to TRUE, the function will perform the access checks and
  return the site offline status, but not log the user out or display any
  messages.

@return
  FALSE if the site is not in maintenance mode, the user login page is
  displayed, or the user has the 'access site in maintenance mode'
  permission. TRUE for anonymous users not being on the login page when the
  site is in maintenance mode.
```

## Code

```php
function _menu_site_is_offline($check_only = FALSE) {
  // Check if site is in maintenance mode.
  if (variable_get('maintenance_mode', 0)) {
    if (user_access('access site in maintenance mode')) {
      // Ensure that the maintenance mode message is displayed only once
      // (allowing for page redirects) and specifically suppress its display on
      // the maintenance mode settings page.
      if (!$check_only && $_GET['q'] != 'admin/config/development/maintenance') {
        if (user_access('administer site configuration')) {
          drupal_set_message(t('Operating in maintenance mode. <a href="@url">Go online.</a>', array('@url' => url('admin/config/development/maintenance'))), 'status', FALSE);
        }
        else {
          drupal_set_message(t('Operating in maintenance mode.'), 'status', FALSE);
        }
      }
    }
    else {
      return TRUE;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
