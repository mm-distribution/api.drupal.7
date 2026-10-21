# locale_form_comment_form_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 400–410 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L400-L410)
- **Module/theme:** locale
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function locale_form_comment_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function locale_form_comment_form_alter(&$form, &$form_state, $form_id) {
  // If a content type has multilingual support we set the content language as
  // comment language.
  if ($form['language']['#value'] == LANGUAGE_NONE && locale_multilingual_node_type($form['#node']->type)) {
    global $language_content;
    $form['language']['#value'] = $language_content->language;
    $submit_callback = 'locale_field_comment_form_submit';
    array_unshift($form['actions']['preview']['#submit'], $submit_callback);
    array_unshift($form['#submit'], $submit_callback);
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
