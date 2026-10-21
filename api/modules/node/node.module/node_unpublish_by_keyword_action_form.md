# node_unpublish_by_keyword_action_form()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4073–4081 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4073-L4081)
- **Module/theme:** node

## Signature

```php
function node_unpublish_by_keyword_action_form($context)
```

## Documentation

```text
Generates settings form for node_unpublish_by_keyword_action().

@param array $context
  Array of additional information about what triggered this action.

@return array
  A form array.

@see node_unpublish_by_keyword_action_submit()
```

## Code

```php
function node_unpublish_by_keyword_action_form($context) {
  $form['keywords'] = array(
    '#title' => t('Keywords'),
    '#type' => 'textarea',
    '#description' => t('The content will be unpublished if it contains any of the phrases above. Use a case-sensitive, comma-separated list of phrases. Example: funny, bungee jumping, "Company, Inc."'),
    '#default_value' => isset($context['keywords']) ? drupal_implode_tags($context['keywords']) : '',
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
