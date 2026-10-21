# locale_form_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 352–361 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L352-L361)
- **Module/theme:** locale
- **Implements:** [hook_form_alter()](../../system/system.api.php/hook_form_alter.md)

## Signature

```php
function locale_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_alter().

Adds language fields to user forms.
```

## Code

```php
function locale_form_alter(&$form, &$form_state, $form_id) {
  // Only alter user forms if there is more than one language.
  if (drupal_multilingual()) {
    // Display language selector when either creating a user on the admin
    // interface or editing a user account.
    if ($form_id == 'user_register_form' || ($form_id == 'user_profile_form' && $form['#user_category'] == 'account')) {
      locale_language_selector_form($form, $form_state, $form['#user']);
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
