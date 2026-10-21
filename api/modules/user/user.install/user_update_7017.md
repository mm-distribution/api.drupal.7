# user_update_7017()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 879–913 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L879-L913)
- **Module/theme:** user
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function user_update_7017()
```

## Documentation

```text
Update email templates to use new tokens.

This function upgrades customized email templates from the old !token format
to the new core tokens format. Additionally, in Drupal 7 we no longer e-mail
plain text passwords to users, and there is no token for a plain text
password in the new token system. Therefore, it also modifies any saved
templates using the old '!password' token such that the token is removed, and
displays a warning to users that they may need to go and modify the wording
of their templates.
```

## Code

```php
function user_update_7017() {
  $message = '';

  $tokens = array(
    '!site' => '[site:name]',
    '!username' => '[user:name]',
    '!mailto' => '[user:mail]',
    '!login_uri' => '[site:login-url]',
    '!uri_brief' => '[site:url-brief]',
    '!edit_uri' => '[user:edit-url]',
    '!login_url' => '[user:one-time-login-url]',
    '!uri' => '[site:url]',
    '!date' => '[date:medium]',
    '!password' => '',
  );

  $result = db_select('variable', 'v')
    ->fields('v', array('name'))
    ->condition('name', db_like('user_mail_') . '%', 'LIKE')
    ->execute();

  foreach ($result as $row) {
    // Use variable_get() to get the unserialized value for free.
    if ($value = variable_get($row->name, FALSE)) {

      if (empty($message) && (strpos($value, '!password') !== FALSE)) {
        $message = t('The ability to send users their passwords in plain text has been removed in Drupal 7. Your existing email templates have been modified to remove it. You should <a href="@template-url">review these templates</a> to make sure they read properly.', array('@template-url' => url('admin/config/people/accounts')));
      }

      variable_set($row->name, str_replace(array_keys($tokens), $tokens, $value));
    }
  }

  return $message;
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
