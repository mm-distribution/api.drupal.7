# forum_form_taxonomy_form_term_alter()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 615–621 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L615-L621)
- **Module/theme:** forum
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function forum_form_taxonomy_form_term_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for taxonomy_form_term().
```

## Code

```php
function forum_form_taxonomy_form_term_alter(&$form, &$form_state, $form_id) {
   $vid = variable_get('forum_nav_vocabulary', 0);
   if (isset($form['vid']['#value']) && $form['vid']['#value'] == $vid) {
    // Hide multiple parents select from forum terms.
    $form['relations']['parent']['#access'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
