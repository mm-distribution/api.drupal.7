# forum_form_taxonomy_form_vocabulary_alter()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 596–610 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L596-L610)
- **Module/theme:** forum
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function forum_form_taxonomy_form_vocabulary_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for taxonomy_form_vocabulary().
```

## Code

```php
function forum_form_taxonomy_form_vocabulary_alter(&$form, &$form_state, $form_id) {
  $vid = variable_get('forum_nav_vocabulary', 0);
  if (isset($form['vid']['#value']) && $form['vid']['#value'] == $vid) {
    $form['help_forum_vocab'] = array(
      '#markup' => t('This is the designated forum vocabulary. Some of the normal vocabulary options have been removed.'),
      '#weight' => -1,
    );
    // Forum's vocabulary always has single hierarchy. Forums and containers
    // have only one parent or no parent for root items. By default this value
    // is 0.
    $form['hierarchy']['#value'] = 1;
    // Do not allow to delete forum's vocabulary.
    $form['actions']['delete']['#access'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
