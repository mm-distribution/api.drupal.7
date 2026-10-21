# openid_form_user_register_form_alter()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 182–237 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L182-L237)
- **Module/theme:** openid
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function openid_form_user_register_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

Prefills the login form with values acquired via OpenID.
```

## Code

```php
function openid_form_user_register_form_alter(&$form, &$form_state) {
  if (isset($_SESSION['openid']['response'])) {
    module_load_include('inc', 'openid');

    $response = $_SESSION['openid']['response'];

    // Extract Simple Registration keys from the response. We only include
    // signed keys as required by OpenID Simple Registration Extension 1.0,
    // section 4.
    $sreg_values = openid_extract_namespace($response, OPENID_NS_SREG, 'sreg', TRUE);
    // Extract Attribute Exchanges keys from the response. We only include
    // signed keys. This is not required by the specification, but it is
    // recommended by Google, see
    // http://googlecode.blogspot.com/2011/05/security-advisory-to-websites-using.html
    $ax_values = openid_extract_namespace($response, OPENID_NS_AX, 'ax', TRUE);

    if (!empty($sreg_values['nickname'])) {
      // Use the nickname returned by Simple Registration if available.
      $form['account']['name']['#default_value'] = $sreg_values['nickname'];
    }
    elseif ($ax_name_values = openid_extract_ax_values($ax_values, array('http://axschema.org/namePerson/friendly', 'http://schema.openid.net/namePerson/friendly'))) {
      // Else, use the first nickname returned by AX if available.
      $form['account']['name']['#default_value'] = current($ax_name_values);
    }
    else {
      $form['account']['name']['#default_value'] = '';
    }

    if (!empty($sreg_values['email'])) {
      // Use the email returned by Simple Registration if available.
      $form['account']['mail']['#default_value'] = $sreg_values['email'];
    }
    elseif ($ax_mail_values = openid_extract_ax_values($ax_values, array('http://axschema.org/contact/email', 'http://schema.openid.net/contact/email'))) {
      // Else, use the first nickname returned by AX if available.
      $form['account']['mail']['#default_value'] = current($ax_mail_values);
    }

    // If user_email_verification is off, hide the password field and just fill
    // with random password to avoid confusion.
    if (!variable_get('user_email_verification', TRUE)) {
      $form['account']['pass']['#type'] = 'hidden';
      $form['account']['pass']['#value'] = user_password();
    }

    $form['openid_claimed_id'] = array(
      '#type' => 'value',
      '#default_value' => $response['openid.claimed_id'],
    );
    $form['openid_display'] = array(
      '#type' => 'item',
      '#title' => t('Your OpenID'),
      '#description' => t('This OpenID will be attached to your account after registration.'),
      '#markup' => check_plain($response['openid.claimed_id']),
    );
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
