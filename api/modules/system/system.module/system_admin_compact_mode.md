# system_admin_compact_mode()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2971–2975 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2971-L2975)
- **Module/theme:** system

## Signature

```php
function system_admin_compact_mode()
```

## Documentation

```text
Determines whether the current user is in compact mode.

Compact mode shows certain administration pages with less description text,
such as the configuration page and the permissions page.

Whether the user is in compact mode is determined by a cookie, which is set
for the user by system_admin_compact_page().

If the user does not have the cookie, the default value is given by the
system variable 'admin_compact_mode', which itself defaults to FALSE. This
does not have a user interface to set it: it is a hidden variable which can
be set in the settings.php file.

@return
  TRUE when in compact mode, FALSE when in expanded mode.
```

## Code

```php
function system_admin_compact_mode() {
  // PHP converts dots into underscores in cookie names to avoid problems with
  // its parser, so we use a converted cookie name.
  return isset($_COOKIE['Drupal_visitor_admin_compact_mode']) ? $_COOKIE['Drupal_visitor_admin_compact_mode'] : variable_get('admin_compact_mode', FALSE);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
