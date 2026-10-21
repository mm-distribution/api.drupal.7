# contact_personal_form()

- **Type:** Function
- **File:** [`modules/contact/contact.pages.inc`](_file.md), lines 183–251 · [local source](../../../../source/modules/contact/contact.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.pages.inc#L183-L251)
- **Module/theme:** contact
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function contact_personal_form($form, &$form_state, $recipient)
```

## Documentation

```text
Form constructor for the personal contact form.

Path: user/%user/contact

@see contact_menu()
@see contact_personal_form_validate()
@see contact_personal_form_submit()
@ingroup forms
```

## Code

```php
function contact_personal_form($form, &$form_state, $recipient) {
  global $user;

  // Check if flood control has been activated for sending e-mails.
  $limit = variable_get('contact_threshold_limit', 5);
  $window = variable_get('contact_threshold_window', 3600);
  if (!flood_is_allowed('contact', $limit, $window) && !user_access('administer contact forms') && !user_access('administer users')) {
    drupal_set_message(t("You cannot send more than %limit messages in @interval. Try again later.", array('%limit' => $limit, '@interval' => format_interval($window))), 'error');
    drupal_access_denied();
    drupal_exit();
  }

  drupal_set_title(t('Contact @username', array('@username' => format_username($recipient))), PASS_THROUGH);

  if (!$user->uid) {
    $form['#attached']['library'][] = array('system', 'jquery.cookie');
    $form['#attributes']['class'][] = 'user-info-from-cookie';
  }

  $form['#attributes']['class'][] = 'contact-form';
  $form['recipient'] = array(
    '#type' => 'value',
    '#value' => $recipient,
  );
  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Your name'),
    '#maxlength' => 255,
    '#default_value' => $user->uid ? format_username($user) : '',
    '#required' => TRUE,
  );
  $form['mail'] = array(
    '#type' => 'textfield',
    '#title' => t('Your e-mail address'),
    '#maxlength' => 255,
    '#default_value' => $user->uid ? $user->mail : '',
    '#required' => TRUE,
  );
  $form['to'] = array(
    '#type' => 'item',
    '#title' => t('To'),
    '#markup' => theme('username', array('account' => $recipient)),
  );
  $form['subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#maxlength' => 50,
    '#required' => TRUE,
  );
  $form['message'] = array(
    '#type' => 'textarea',
    '#title' => t('Message'),
    '#rows' => 15,
    '#required' => TRUE,
  );
  // We do not allow anonymous users to send themselves a copy
  // because it can be abused to spam people.
  $form['copy'] = array(
    '#type' => 'checkbox',
    '#title' => t('Send yourself a copy.'),
    '#access' => $user->uid,
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Send message'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/contact/contact.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
