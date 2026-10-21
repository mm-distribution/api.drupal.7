# contact_personal_form_submit()

- **Type:** Function
- **File:** [`modules/contact/contact.pages.inc`](_file.md), lines 269–300 · [local source](../../../../source/modules/contact/contact.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.pages.inc#L269-L300)
- **Module/theme:** contact

## Signature

```php
function contact_personal_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for contact_personal_form().

@see contact_personal_form_validate()
```

## Code

```php
function contact_personal_form_submit($form, &$form_state) {
  global $user, $language;

  $values = $form_state['values'];
  $values['sender'] = clone $user;
  $values['sender']->name = $values['name'];
  $values['sender']->mail = $values['mail'];

  // Save the anonymous user information to a cookie for reuse.
  if (!$user->uid) {
    user_cookie_save(array_intersect_key($values, array_flip(array('name', 'mail'))));
  }

  // Get the to and from e-mail addresses.
  $to = $values['recipient']->mail;
  $from = $values['sender']->mail;

  // Send the e-mail in the requested user language.
  drupal_mail('contact', 'user_mail', $to, user_preferred_language($values['recipient']), $values, $from);

  // Send a copy if requested, using current page language.
  if ($values['copy']) {
    drupal_mail('contact', 'user_copy', $from, $language, $values, $from);
  }

  flood_register_event('contact', variable_get('contact_threshold_window', 3600));
  watchdog('mail', '%sender-name (@sender-from) sent %recipient-name an e-mail.', array('%sender-name' => $values['name'], '@sender-from' => $from, '%recipient-name' => $values['recipient']->name));

  // Jump to the contacted user's profile page.
  drupal_set_message(t('Your message has been sent.'));
  $form_state['redirect'] = user_access('access user profiles') ? 'user/' . $values['recipient']->uid : '';
}
```

---
_Drupal 7.103 · [modules/contact/contact.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
