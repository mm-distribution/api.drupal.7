# drupal_anonymous_user()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2513–2521 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2513-L2521)

## Signature

```php
function drupal_anonymous_user()
```

## Documentation

```text
Generates a default anonymous $user object.

@return Object - the user object.
```

## Code

```php
function drupal_anonymous_user() {
  $user = variable_get('drupal_anonymous_user_object', new stdClass);
  $user->uid = 0;
  $user->hostname = ip_address();
  $user->roles = array();
  $user->roles[DRUPAL_ANONYMOUS_RID] = 'anonymous user';
  $user->cache = 0;
  return $user;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
