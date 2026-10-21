# locale_language_selector_form()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 277–306 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L277-L306)
- **Module/theme:** locale
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function locale_language_selector_form(&$form, &$form_state, $user)
```

## Documentation

```text
Form builder callback to display language selection widget.

@ingroup forms
@see locale_form_alter()
```

## Code

```php
function locale_language_selector_form(&$form, &$form_state, $user) {
  global $language;
  $languages = language_list('enabled');
  $languages = $languages[1];

  // If the user is being created, we set the user language to the page language.
  $user_preferred_language = $user->uid ? user_preferred_language($user) : $language;

  $names = array();
  foreach ($languages as $langcode => $item) {
    $name = t($item->name);
    $names[$langcode] = $name . ($item->native != $name ? ' (' . $item->native . ')' : '');
  }
  $form['locale'] = array(
    '#type' => 'fieldset',
    '#title' => t('Language settings'),
    '#weight' => 1,
    '#access' => ($form['#user_category'] == 'account' || ($form['#user_category'] == 'register' && user_access('administer users'))),
  );

  // Get language negotiation settings.
  $mode = language_negotiation_get(LANGUAGE_TYPE_INTERFACE) != LANGUAGE_NEGOTIATION_DEFAULT;
  $form['locale']['language'] = array(
    '#type' => (count($names) <= 5 ? 'radios' : 'select'),
    '#title' => t('Language'),
    '#default_value' => $user_preferred_language->language,
    '#options' => $names,
    '#description' => $mode ? t("This account's default language for e-mails, and preferred language for site presentation.") : t("This account's default language for e-mails."),
  );
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
