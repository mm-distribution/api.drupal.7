# locale_translate_edit_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1108–1170 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1108-L1170)
- **Module/theme:** locale
- **Topics:** [locale-translate-edit-delete](../../../topics/locale-translate-edit-delete.md)

## Signature

```php
function locale_translate_edit_form($form, &$form_state, $lid)
```

## Documentation

```text
User interface for string editing.
```

## Code

```php
function locale_translate_edit_form($form, &$form_state, $lid) {
  // Fetch source string, if possible.
  $source = db_query('SELECT source, context, textgroup, location FROM {locales_source} WHERE lid = :lid', array(':lid' => $lid))->fetchObject();
  if (!$source) {
    drupal_set_message(t('String not found.'), 'error');
    drupal_goto('admin/config/regional/translate/translate');
  }

  // Add original text to the top and some values for form altering.
  $form['original'] = array(
    '#type'  => 'item',
    '#title' => t('Original text'),
    '#markup' => check_plain(wordwrap($source->source, 0)),
  );
  if (!empty($source->context)) {
    $form['context'] = array(
      '#type' => 'item',
      '#title' => t('Context'),
      '#markup' => check_plain($source->context),
    );
  }
  $form['lid'] = array(
    '#type'  => 'value',
    '#value' => $lid
  );
  $form['textgroup'] = array(
    '#type'  => 'value',
    '#value' => $source->textgroup,
  );
  $form['location'] = array(
    '#type'  => 'value',
    '#value' => $source->location
  );

  // Include both translated and not yet translated target languages in the
  // list. The source language is English for built-in strings and the default
  // language for other strings.
  $languages = language_list();
  $default = language_default();
  $omit = $source->textgroup == 'default' ? 'en' : $default->language;
  unset($languages[($omit)]);
  $form['translations'] = array('#tree' => TRUE);
  // Approximate the number of rows to use in the default textarea.
  $rows = min(ceil(str_word_count($source->source) / 12), 10);
  foreach ($languages as $langcode => $language) {
    $form['translations'][$langcode] = array(
      '#type' => 'textarea',
      '#title' => t($language->name),
      '#rows' => $rows,
      '#default_value' => '',
    );
  }

  // Fetch translations and fill in default values in the form.
  $result = db_query("SELECT DISTINCT translation, language FROM {locales_target} WHERE lid = :lid AND language <> :omit", array(':lid' => $lid, ':omit' => $omit));
  foreach ($result as $translation) {
    $form['translations'][$translation->language]['#default_value'] = $translation->translation;
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save translations'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
