# taxonomy_overview_vocabularies_submit()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 50–58 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L50-L58)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_overview_vocabularies_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for vocabularies overview. Updates changed vocabulary weights.

@see taxonomy_overview_vocabularies()
```

## Code

```php
function taxonomy_overview_vocabularies_submit($form, &$form_state) {
  foreach ($form_state['values'] as $vid => $vocabulary) {
    if (is_numeric($vid) && $form[$vid]['#vocabulary']->weight != $form_state['values'][$vid]['weight']) {
      $form[$vid]['#vocabulary']->weight = $form_state['values'][$vid]['weight'];
      taxonomy_vocabulary_save($form[$vid]['#vocabulary']);
    }
  }
  drupal_set_message(t('The configuration options have been saved.'));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
