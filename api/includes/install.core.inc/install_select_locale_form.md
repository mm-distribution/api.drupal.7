# install_select_locale_form()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1322–1349 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1322-L1349)
- **Topics:** [forms](../../topics/forms.md)

## Signature

```php
function install_select_locale_form($form, &$form_state, $locales, $profilename)
```

## Documentation

```text
Form constructor for the language selection form.

@ingroup forms
```

## Code

```php
function install_select_locale_form($form, &$form_state, $locales, $profilename) {
  include_once DRUPAL_ROOT . '/includes/iso.inc';
  $languages = _locale_get_predefined_list();
  foreach ($locales as $locale) {
    $name = $locale->langcode;
    if (isset($languages[$name])) {
      $name = $languages[$name][0] . (isset($languages[$name][1]) ? ' ' . st('(@language)', array('@language' => $languages[$name][1])) : '');
    }
    $form['locale'][$locale->langcode] = array(
      '#type' => 'radio',
      '#return_value' => $locale->langcode,
      '#default_value' => $locale->langcode == 'en' ? 'en' : '',
      '#title' => $name . ($locale->langcode == 'en' ? ' ' . st('(built-in)') : ''),
      '#parents' => array('locale')
    );
  }
  if (count($locales) == 1) {
    $form['help'] = array(
      '#markup' => '<p><a href="install.php?profile=' . $profilename . '&amp;localize=true">' . st('Learn how to install Drupal in other languages') . '</a></p>',
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] =  array(
    '#type' => 'submit',
    '#value' => st('Save and continue'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
