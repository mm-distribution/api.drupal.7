# hook_search_admin()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 108–130 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L108-L130)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_admin()
```

## Documentation

```text
Add elements to the search settings form.

@return
  Form array for the Search settings page at admin/config/search/settings.

@ingroup search
```

## Code

```php
function hook_search_admin() {
  // Output form for defining rank factor weights.
  $form['content_ranking'] = array(
    '#type' => 'fieldset',
    '#title' => t('Content ranking'),
  );
  $form['content_ranking']['#theme'] = 'node_search_admin';
  $form['content_ranking']['info'] = array(
    '#value' => '<em>' . t('The following numbers control which properties the content search should favor when ordering the results. Higher numbers mean more influence, zero means the property is ignored. Changing these numbers does not require the search index to be rebuilt. Changes take effect immediately.') . '</em>'
  );

  // Note: reversed to reflect that higher number = higher ranking.
  $options = drupal_map_assoc(range(0, 10));
  foreach (module_invoke_all('ranking') as $var => $values) {
    $form['content_ranking']['factors']['node_rank_' . $var] = array(
      '#title' => $values['title'],
      '#type' => 'select',
      '#options' => $options,
      '#default_value' => variable_get('node_rank_' . $var, 0),
    );
  }
  return $form;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_admin()".

- [node_search_admin()](../../node/node.module/node_search_admin.md) — `modules/node/node.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
