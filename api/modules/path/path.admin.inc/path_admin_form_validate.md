# path_admin_form_validate()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 196–217 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L196-L217)
- **Module/theme:** path

## Signature

```php
function path_admin_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for path_admin_form().

@see path_admin_form_submit()
@see path_admin_form_delete_submit()
```

## Code

```php
function path_admin_form_validate($form, &$form_state) {
  $source = &$form_state['values']['source'];
  $source = drupal_get_normal_path($source);
  $alias = $form_state['values']['alias'];
  $pid = isset($form_state['values']['pid']) ? $form_state['values']['pid'] : 0;
  // Language is only set if locale module is enabled, otherwise save for all languages.
  $language = isset($form_state['values']['language']) ? $form_state['values']['language'] : LANGUAGE_NONE;

  $has_alias = db_query("SELECT COUNT(alias) FROM {url_alias} WHERE pid <> :pid AND alias = :alias AND language = :language", array(
      ':pid' => $pid,
      ':alias' => $alias,
      ':language' => $language,
    ))
    ->fetchField();

  if ($has_alias) {
    form_set_error('alias', t('The alias %alias is already in use in this language.', array('%alias' => $alias)));
  }
  if (!drupal_valid_path($source)) {
    form_set_error('source', t("The path '@link_path' is either invalid or you do not have access to it.", array('@link_path' => $source)));
  }
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
