# user_tokens()

- **Type:** Function
- **File:** [`modules/user/user.tokens.inc`](_file.md), lines 70–151 · [local source](../../../../source/modules/user/user.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.tokens.inc#L70-L151)
- **Module/theme:** user
- **Implements:** [hook_tokens()](../../system/system.api.php/hook_tokens.md)

## Signature

```php
function user_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function user_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $url_options = array('absolute' => TRUE);
  if (isset($options['language'])) {
    $url_options['language'] = $options['language'];
    $language_code = $options['language']->language;
  }
  else {
    $language_code = NULL;
  }
  $sanitize = !empty($options['sanitize']);

  $replacements = array();

  if ($type == 'user' && !empty($data['user'])) {
    $account = $data['user'];
    foreach ($tokens as $name => $original) {
      switch ($name) {
        // Basic user account information.
        case 'uid':
          // In the case of hook user_presave uid is not set yet.
          $replacements[$original] = !empty($account->uid) ? $account->uid : t('not yet assigned');
          break;

        case 'name':
          $name = format_username($account);
          $replacements[$original] = $sanitize ? check_plain($name) : $name;
          break;

        case 'mail':
          if (empty($account->mail)) {
            $replacements[$original] = '';
          }
          else {
            $replacements[$original] = $sanitize ? check_plain($account->mail) : $account->mail;
          }
          break;

        case 'url':
          $replacements[$original] = !empty($account->uid) ? url("user/$account->uid", $url_options) : t('not yet assigned');
          break;

        case 'edit-url':
          $replacements[$original] = !empty($account->uid) ? url("user/$account->uid/edit", $url_options) : t('not yet assigned');
          break;

        // These tokens are default variations on the chained tokens handled below.
        case 'last-login':
          $replacements[$original] = !empty($account->login) ? format_date($account->login, 'medium', '', NULL, $language_code) : t('never');
          break;

        case 'created':
          // In the case of user_presave the created date may not yet be set.
          $replacements[$original] = !empty($account->created) ? format_date($account->created, 'medium', '', NULL, $language_code) : t('not yet created');
          break;

        case 'changed':
          // In the case of user_presave the created date may not yet be set.
          $replacements[$original] = !empty($account->changed) ? format_date($account->changed, 'medium', '', NULL, $language_code) : t('not yet created');
          break;
      }
    }

    if ($login_tokens = token_find_with_prefix($tokens, 'last-login')) {
      $replacements += token_generate('date', $login_tokens, array('date' => $account->login), $options);
    }

    if ($registered_tokens = token_find_with_prefix($tokens, 'created')) {
      $replacements += token_generate('date', $registered_tokens, array('date' => $account->created), $options);
    }

    if ($changed_tokens = token_find_with_prefix($tokens, 'changed')) {
      $replacements += token_generate('date', $changed_tokens, array('date' => $account->changed), $options);
    }
  }

  if ($type == 'current-user') {
    $account = user_load($GLOBALS['user']->uid);
    $replacements += token_generate('user', $tokens, array('user' => $account), $options);
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/user/user.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
