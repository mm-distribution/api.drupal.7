# node_search_validate()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2884–2923 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2884-L2923)
- **Module/theme:** node

## Signature

```php
function node_search_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for node_form_alter().
```

## Code

```php
function node_search_validate($form, &$form_state) {
  // Initialize using any existing basic search keywords.
  $keys = $form_state['values']['processed_keys'];

  // Insert extra restrictions into the search keywords string.
  if (isset($form_state['values']['type']) && is_array($form_state['values']['type'])) {
    // Retrieve selected types - Form API sets the value of unselected
    // checkboxes to 0.
    $form_state['values']['type'] = array_filter($form_state['values']['type']);
    if (count($form_state['values']['type'])) {
      $keys = search_expression_insert($keys, 'type', implode(',', array_keys($form_state['values']['type'])));
    }
  }

  if (isset($form_state['values']['term']) && is_array($form_state['values']['term']) && count($form_state['values']['term'])) {
    $keys = search_expression_insert($keys, 'term', implode(',', $form_state['values']['term']));
  }
  if (isset($form_state['values']['language']) && is_array($form_state['values']['language'])) {
    $languages = array_filter($form_state['values']['language']);
    if (count($languages)) {
      $keys = search_expression_insert($keys, 'language', implode(',', $languages));
    }
  }
  if ($form_state['values']['or'] != '') {
    if (preg_match_all('/ ("[^"]+"|[^" ]+)/i', ' ' . $form_state['values']['or'], $matches)) {
      $keys .= ' ' . implode(' OR ', $matches[1]);
    }
  }
  if ($form_state['values']['negative'] != '') {
    if (preg_match_all('/ ("[^"]+"|[^" ]+)/i', ' ' . $form_state['values']['negative'], $matches)) {
      $keys .= ' -' . implode(' -', $matches[1]);
    }
  }
  if ($form_state['values']['phrase'] != '') {
    $keys .= ' "' . str_replace('"', ' ', $form_state['values']['phrase']) . '"';
  }
  if (!empty($keys)) {
    form_set_value($form['basic']['processed_keys'], trim($keys), $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
