# format_username()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2225–2229 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2225-L2229)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_username($account)
```

## Documentation

```text
Format a username.

This is also the label callback implementation of
callback_entity_info_label() for user_entity_info().

By default, the passed-in object's 'name' property is used if it exists, or
else, the site-defined value for the 'anonymous' variable. However, a module
may override this by implementing hook_username_alter(&$name, $account).

@see hook_username_alter()

@param $account
  The account object for the user whose name is to be formatted.

@return
  An unsanitized string with the username to display. The code receiving
  this result must ensure that check_plain() is called on it before it is
  printed to the page.
```

## Code

```php
function format_username($account) {
  $name = !empty($account->name) ? $account->name : variable_get('anonymous', t('Anonymous'));
  drupal_alter('username', $name, $account);
  return $name;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
