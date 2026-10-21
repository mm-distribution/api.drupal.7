# contact_form_user_profile_form_alter()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 215–231 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L215-L231)
- **Module/theme:** contact
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function contact_form_user_profile_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

Add the enable personal contact form to an individual user's account page.

@see user_profile_form()
```

## Code

```php
function contact_form_user_profile_form_alter(&$form, &$form_state) {
  if ($form['#user_category'] == 'account') {
    $account = $form['#user'];
    $form['contact'] = array(
      '#type' => 'fieldset',
      '#title' => t('Contact settings'),
      '#weight' => 5,
      '#collapsible' => TRUE,
    );
    $form['contact']['contact'] = array(
      '#type' => 'checkbox',
      '#title' => t('Personal contact form'),
      '#default_value' => !empty($account->data['contact']) ? $account->data['contact'] : FALSE,
      '#description' => t('Allow other users to contact you via a <a href="@url">personal contact form</a> which keeps your e-mail address hidden. Note that some privileged users such as site administrators are still able to contact you even if you choose to disable this feature.', array('@url' => url("user/$account->uid/contact"))),
    );
  }
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
