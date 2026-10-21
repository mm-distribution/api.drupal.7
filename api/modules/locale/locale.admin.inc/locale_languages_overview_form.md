# locale_languages_overview_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 20–62 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L20-L62)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_overview_form()
```

## Documentation

```text
User interface for the language overview screen.
```

## Code

```php
function locale_languages_overview_form() {
  drupal_static_reset('language');
  $languages = language_list('language');

  $options = array();
  $form['weight'] = array('#tree' => TRUE);
  foreach ($languages as $langcode => $language) {

    $options[$langcode] = '';
    if ($language->enabled) {
      $enabled[] = $langcode;
    }
    $form['weight'][$langcode] = array(
      '#type' => 'weight',
      '#title' => t('Weight for @title', array('@title' => $language->name)),
      '#title_display' => 'invisible',
      '#default_value' => $language->weight,
      '#attributes' => array('class' => array('language-order-weight')),
    );
    $form['name'][$langcode] = array('#markup' => check_plain($language->name));
    $form['native'][$langcode] = array('#markup' => check_plain($language->native));
    $form['direction'][$langcode] = array('#markup' => ($language->direction == LANGUAGE_RTL ? t('Right to left') : t('Left to right')));
  }
  $form['enabled'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Enabled languages'),
    '#title_display' => 'invisible',
    '#options' => $options,
    '#default_value' => $enabled,
  );
  $form['site_default'] = array(
    '#type' => 'radios',
    '#title' => t('Default language'),
    '#title_display' => 'invisible',
    '#options' => $options,
    '#default_value' => language_default('language'),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save configuration'));
  $form['#theme'] = 'locale_languages_overview_form';

  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
