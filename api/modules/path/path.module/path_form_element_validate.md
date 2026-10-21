# path_form_element_validate()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 153–183 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L153-L183)
- **Module/theme:** path

## Signature

```php
function path_form_element_validate($element, &$form_state, $complete_form)
```

## Documentation

```text
Form element validation handler for URL alias form element.

@see path_form_node_form_alter()
```

## Code

```php
function path_form_element_validate($element, &$form_state, $complete_form) {
  // Trim the submitted value.
  $alias = trim($form_state['values']['path']['alias']);
  if (!empty($alias)) {
    form_set_value($element['alias'], $alias, $form_state);
    // Node language (Locale module) needs special care. Since the language of
    // the URL alias depends on the node language, and the node language can be
    // switched right within the same form, we need to conditionally overload
    // the originally assigned URL alias language.
    // @todo Remove this after converting Path module to a field, and, after
    //   stopping Locale module from abusing the content language system.
    if (isset($form_state['values']['language'])) {
      form_set_value($element['language'], $form_state['values']['language'], $form_state);
    }

    $path = $form_state['values']['path'];

    // Ensure that the submitted alias does not exist yet.
    $query = db_select('url_alias')
      ->condition('alias', $path['alias'])
      ->condition('language', $path['language']);
    if (!empty($path['source'])) {
      $query->condition('source', $path['source'], '<>');
    }
    $query->addExpression('1');
    $query->range(0, 1);
    if ($query->execute()->fetchField()) {
      form_error($element, t('The alias is already in use.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
