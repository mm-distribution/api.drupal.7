# openid_menu()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 11–37 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L11-L37)
- **Module/theme:** openid
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function openid_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function openid_menu() {
  $items['openid/authenticate'] = array(
    'title' => 'OpenID Login',
    'page callback' => 'openid_authentication_page',
    'access callback' => 'user_is_anonymous',
    'type' => MENU_CALLBACK,
    'file' => 'openid.pages.inc',
  );
  $items['user/%user/openid'] = array(
    'title' => 'OpenID identities',
    'page callback' => 'openid_user_identities',
    'page arguments' => array(1),
    'access callback' => 'user_edit_access',
    'access arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'file' => 'openid.pages.inc',
  );
  $items['user/%user/openid/delete'] = array(
    'title' => 'Delete OpenID',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('openid_user_delete_form', 1),
    'access callback' => 'user_edit_access',
    'access arguments' => array(1),
    'file' => 'openid.pages.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
