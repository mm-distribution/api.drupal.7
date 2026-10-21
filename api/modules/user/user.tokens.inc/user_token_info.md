# user_token_info()

- **Type:** Function
- **File:** [`modules/user/user.tokens.inc`](_file.md), lines 11–65 · [local source](../../../../source/modules/user/user.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.tokens.inc#L11-L65)
- **Module/theme:** user
- **Implements:** [hook_token_info()](../../system/system.api.php/hook_token_info.md)

## Signature

```php
function user_token_info()
```

## Documentation

```text
Implements hook_token_info().
```

## Code

```php
function user_token_info() {
  $types['user'] = array(
    'name' => t('Users'),
    'description' => t('Tokens related to individual user accounts.'),
    'needs-data' => 'user',
  );
  $types['current-user'] = array(
    'name' => t('Current user'),
    'description' => t('Tokens related to the currently logged in user.'),
    'type' => 'user',
  );

  $user['uid'] = array(
    'name' => t('User ID'),
    'description' => t("The unique ID of the user account."),
  );
  $user['name'] = array(
    'name' => t("Name"),
    'description' => t("The login name of the user account."),
  );
  $user['mail'] = array(
    'name' => t("Email"),
    'description' => t("The email address of the user account."),
  );
  $user['url'] = array(
    'name' => t("URL"),
    'description' => t("The URL of the account profile page."),
  );
  $user['edit-url'] = array(
    'name' => t("Edit URL"),
    'description' => t("The URL of the account edit page."),
  );

  $user['last-login'] = array(
    'name' => t("Last login"),
    'description' => t("The date the user last logged in to the site."),
    'type' => 'date',
  );
  $user['created'] = array(
    'name' => t("Created"),
    'description' => t("The date the user account was created."),
    'type' => 'date',
  );

  $user['changed'] = array(
    'name' => t("Changed"),
    'description' => t("The date the user account was changed."),
    'type' => 'date',
  );

  return array(
    'types' => $types,
    'tokens' => array('user' => $user),
  );
}
```

---
_Drupal 7.103 · [modules/user/user.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
