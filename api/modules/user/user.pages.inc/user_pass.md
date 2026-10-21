# user_pass()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 30–61 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L30-L61)
- **Module/theme:** user
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function user_pass()
```

## Documentation

```text
Form builder; Request a password reset.

@ingroup forms
@see user_pass_validate()
@see user_pass_submit()
```

## Code

```php
function user_pass() {
  global $user;

  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Username or e-mail address'),
    '#size' => 60,
    '#maxlength' => max(USERNAME_MAX_LENGTH, EMAIL_MAX_LENGTH),
    '#required' => TRUE,
    '#default_value' => isset($_GET['name']) ? $_GET['name'] : '',
  );
  // Allow logged in users to request this also.
  if ($user->uid > 0) {
    $form['name']['#type'] = 'value';
    $form['name']['#value'] = $user->mail;
    $form['mail'] = array(
      '#prefix' => '<p>',
      // As of https://www.drupal.org/node/889772 the user no longer must log
      // out (if they are still logged in when using the password reset link,
      // they will be logged out automatically then), but this text is kept as
      // is to avoid breaking translations as well as to encourage the user to
      // log out manually at a time of their own choosing (when it will not
      // interrupt anything else they may have been in the middle of doing).
      '#markup' =>  t('Password reset instructions will be mailed to %email. You must log out to use the password reset link in the e-mail.', array('%email' => $user->mail)),
      '#suffix' => '</p>',
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('E-mail new password'));

  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
